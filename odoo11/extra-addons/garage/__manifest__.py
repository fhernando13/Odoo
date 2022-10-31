# -*- coding: utf-8 -*-
{
    'name': "garage",

    'summary': """
        Administracion de garage
        """,

    'description': """
        Modulo para administrar autos, estacionamientos y mantenimientos
    """,

    'author': "Fers",
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
        'views/garage_auto.xml',
        'views/garage_modelo_moto.xml',
        'views/garage_marca_moto.xml',
        'views/garage_registro_moto.xml',
        'views/garage_mantenimiento.xml',
        'views/garage_estacionamiento.xml',
        'views/garage_report.xml',
        'views/menu.xml',
        # 'report/garage_report_wizard.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}