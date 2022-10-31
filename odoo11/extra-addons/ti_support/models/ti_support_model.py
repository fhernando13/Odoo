# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ti_support_model(models.Model):
    _name = 'ti_support.ti_support_model'

    name = fields.Char(string='Modelo', required=True)
    name_id = fields.Many2one(comodel_name='ti_support.ti_support_brand', string='Marca', requiered=True)
    anio = fields.Integer(string='Año', required=True)

    @api.constrains('name')
    def check_name(self):
        for rec in self:
            brand = self.env['ti_support.ti_support_brand'].search([('name', '=', rec.name), ('id', '!=', rec.id)])
            if brand:
                raise ValidationError("Modelo %s ya existe" % rec.name)
    

    @api.model
    def create(self, values):
        # Add code here
        res = super(ti_support_model, self).create(self.upper_dict(values))
        return res
    
    
    @api.multi
    def write(self, values):
        # CODE HERE
        return super(ti_support_model, self).write(self.upper_dict(values))
    
    
    def upper_dict(self,vals):
        upper_values = {}
        for k, v in vals.items():
            if isinstance(v, str):
                upper_values.update({k:v.upper()})
            else:
                upper_values.update({k:v})
        return upper_values