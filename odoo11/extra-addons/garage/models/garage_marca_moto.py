# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class marca_moto(models.Model):
    _name = 'garage.marca_moto'
    _description = 'Registro de marcas de motocicletas'
    _order='name'
    
    name = fields.Char(string='Marca', required=True)

    @api.constrains('name')
    def check_name(self):
        for rec in self:
            brand = self.env['garage.marca_moto'].search([('name', '=', rec.name), ('id', '!=', rec.id)])
            if brand:
                raise ValidationError("Marca %s ya existe" % rec.name)
    

    @api.model
    def create(self, values):
        # Add code here
        res = super(marca_moto, self).create(self.upper_dict(values))
        return res
    
    
    @api.multi
    def write(self, values):
        # CODE HERE
        return super(marca_moto, self).write(self.upper_dict(values))
    
    
    def upper_dict(self,vals):
        upper_values = {}
        for k, v in vals.items():
            if isinstance(v, str):
                upper_values.update({k:v.upper()})
            else:
                upper_values.update({k:v})
        return upper_values