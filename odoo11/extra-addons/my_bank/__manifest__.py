# -*- coding: utf-8 -*-
{
    'name': "Bancos",

    'summary': """
        Modulo de prueba 2""",

    'description': """
        Modulo de prueba para bancos
    """,

    'author': "4G",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views_balanace_bank.xml',
        'views/views_credit_line.xml',
        'views/view_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}