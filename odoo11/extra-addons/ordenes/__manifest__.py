# -*- coding: utf-8 -*-
{
    'name': "Ordenes de los productos",

    'summary': """
        Registro de ordenes de productos""",

    'description': """
        Aqui se registran las ordenes de los productos por fecha
    """,

    'author': "Fhers",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','tienda'],#nombre de la carpeta

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}