# -*- coding: utf-8 -*-

from odoo import models, fields, api

class pedidos(models.Model):
    _name = 'ordenes.pedidos'

    name = fields.Char(string='Producto', required=True)
    pieces = fields.Integer('Piezas', Required=True) 
    n_p_start_date = fields.Date(string='Fecha de construccion', required=True)
    