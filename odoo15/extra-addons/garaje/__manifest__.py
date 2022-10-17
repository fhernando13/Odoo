# -*- coding: utf-8 -*-
{
    'name': "garaje",

    'summary': """
        Gestion de colleciones de autos en estacionamientos""",

    'description': """
        App de estacionamiento, gestiona autos, usuarios y mas!!!!!!!!!
    """,

    'author': "My Company",
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
        'security/garaje_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/garaje_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}