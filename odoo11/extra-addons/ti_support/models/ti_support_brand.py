# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ti_support_brand(models.Model):
    _name = 'ti_support.ti_support_brand'

    name = fields.Char(string='Marca', required=True)

    @api.constrains('name')
    def check_name(self):
        for rec in self:
            brand = self.env['ti_support.ti_support_brand'].search([('name', '=', rec.name), ('id', '!=', rec.id)])
            if brand:
                raise ValidationError("Marca %s ya existe" % rec.name)
    

    @api.model
    def create(self, values):
        # Add code here
        res = super(ti_support_brand, self).create(self.upper_dict(values))
        return res
    
    
    @api.multi
    def write(self, values):
        # CODE HERE
        return super(ti_support_brand, self).write(self.upper_dict(values))
    
    
    def upper_dict(self,vals):
        upper_values = {}
        for k, v in vals.items():
            if isinstance(v, str):
                upper_values.update({k:v.upper()})
            else:
                upper_values.update({k:v})
        return upper_values