# -*- coding: utf-8 -*-

from odoo import api, fields, models, modules, _

class IrModule(models.Model):
    _inherit = 'ir.module.module'

    local_updatable = fields.Boolean('Local updatable', compute='_compute_local_updatable', store=True)
    addons_path_id = fields.Many2one('ir.module.addons.path', string='Addons Path ID', readonly=True)
    addons_path = fields.Char(string='Addons Path', related='addons_path_id.path', readonly=True)
    license = fields.Char(readonly=True)

    @api.depends('installed_version', 'latest_version')
    def _compute_local_updatable(self):
        default_version = modules.adapt_version('1.0')
        known_mods = self.with_context(lang=None).search([])
        known_mods_names = {mod.name: mod for mod in known_mods}

        for mod in self:
            installed_version = self.get_module_info(mod.name).get('version', default_version)
            if installed_version and mod.latest_version and installed_version > mod.latest_version:
                mod.local_updatable = True
            else:
                mod.local_updatable = False

    def module_multi_uninstall(self):
        """ Perform the various steps required to uninstall a module completely
            including the deletion of all database structures created by the module:
            tables, columns, constraints, etc.
        """
        modules = self.browse(self.env.context.get('active_ids'))
        for module in modules:
            if module.name not in ['base', 'web']:
                module.button_immediate_uninstall()

    def module_multi_refresh_po(self):
        lang = self.env.user.lang
        modules = self.filtered(lambda r: r.state == 'installed')
        modules._update_translations(filter_lang=lang, overwrite=True)
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'target': 'new',
            'params': {
                'message': _("The languages that you selected have been successfully updated. "
                             "You still need to Upgrade the apps to make it work."),
                'type': 'success',
                'sticky': False,
                'next': {'type': 'ir.actions.act_window_close'},
            }
        }

    def button_get_po(self):
        self.ensure_one()
        action = self.env.ref('app_pandora_customize.action_server_module_multi_get_po').sudo().read()[0]
        action['context'].update({
            'default_lang': self.env.user.lang,
        })
        return action

    def update_list(self):
        res = super(IrModule, self).update_list()
        default_version = modules.adapt_version('1.0')
        known_mods = self.with_context(lang=None).search([])
        known_mods_names = {mod.name: mod for mod in known_mods}

        for mod_name in modules.get_modules():
            mod = known_mods_names.get(mod_name)
            installed_version = self.get_module_info(mod.name).get('version', default_version)
            if installed_version and mod.latest_version and installed_version > mod.latest_version:
                local_updatable = True
            else:
                local_updatable = False

            if mod.local_updatable != local_updatable:
                mod.write({'local_updatable': local_updatable})

        return res

