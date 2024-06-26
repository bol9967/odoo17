# -*- coding: utf-8 -*-

# Created on 2023-02-02
##############################################################################
#    Copyright (C) 2009-TODAY outsetx.com Ltd. https://www.outsetx.com
#    Author: OutsetX，hasanchaudharyy@gmail.com
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#    See <http://www.gnu.org/licenses/>.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
##############################################################################

{
    'name': "Pandora Common Util and Tools",
    'version': '24.04.18',
    'author': 'OutsetX',
    'category': 'Base',
    'website': 'https://www.outsetx.com',
    'live_test_url': 'https://outsetx.com',
    'license': 'LGPL-3',
    'sequence': 2,
    'price': 0.00,
    'currency': 'EUR',
    'summary': '''
    Core for common use for pandorarevolution.com apps.
    ''',
    'description': '''
    need to setup odoo.conf, add follow:
    server_wide_modules = web,app_common
    1. Quick import data from excel with .py code
    2. Quick m2o default value
    3. Filter for useless field
    4. UTC local timezone convert
    5. Get browser ua, user-agent
    6. Image to local, image url to local, media to local attachment
    7. Log cron job
    8. Boost for less no use mail
    9. Customize .rng file
    10. Misc like get distance between two points
    11. Multi-language Support. Multi-Company Support.
    13. Full Open Source.
    ==========
    ''',
    'depends': [
        'mail',
        'web',
    ],
    'data': [
        'views/ir_cron_views.xml',
        # 'report/.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'demo': [],
    # 'pre_init_hook': 'pre_init_hook',
    # 'post_init_hook': 'post_init_hook',
    # 'uninstall_hook': 'uninstall_hook',
    # 'external_dependencies': {'python': ['pyyaml', 'ua-parser', 'user-agents']},
    'installable': True,
    'application': True,
    'auto_install': True,
}
