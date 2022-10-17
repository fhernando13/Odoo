# -*- coding: utf-8 -*-

from odoo import models, fields, api

class productos(models.Model):
    _name = 'tienda.productos'
    _description = "productos de tienda"
        
    product = fields.Char(string='Producto', required=True)
    amount = fields.Integer(string='Cantidad',default=0)
    price = fields.Float('Precio', (4,1), default= 0.0, help='Precio del producto')