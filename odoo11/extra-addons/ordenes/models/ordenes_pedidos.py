# -*- coding: utf-8 -*-
from odoo import models, fields, api

class pedidos(models.Model):
    _name = 'ordenes.pedidos'

    name = fields.Char(compute='_compute_name')

    def action_MO(self):
        print('nombre del producto' + str(self.product_id))
    
    def _compute_name(self):
        for record in self:
            record.name = record.product_id.categ_id.complete_name
    
    product_id = fields.Many2one(comodel_name='product.product', string='product')
    pieces = fields.Integer('Piezas', Required=True) 
    n_p_start_date = fields.Date(string='Fecha de construccion', required=True)
    
    
    