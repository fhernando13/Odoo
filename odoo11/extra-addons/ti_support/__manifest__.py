# -*- coding: utf-8 -*-
{
    'name': "Soporte TI",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Changuilu",
    'website': "http://www.changuilu.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'ti_support',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/view_ti_support_hardware.xml',
        'views/view_ti_support_system.xml',
        'views/view_ti_support_assignment.xml',
        'views/view_ti_support_device.xml',
        'views/view_ti_support_brand.xml',
        'views/view_ti_support_model.xml',
        # 'wizard/ti_report_wizard.xml',
        'views/view_ti_support_menu.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application':True,
}