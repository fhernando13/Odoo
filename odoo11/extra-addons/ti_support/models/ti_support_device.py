# -*- coding: utf-8 -*-

from odoo import models, fields, api
import random 


class ti_support_device(models.Model):
    _name = 'ti_support.ti_support_device'

    name = fields.Char(string='Modelo')
    brand_id = fields.Many2one('ti_support.ti_support_brand', string='Marca')  
    type_device = fields.Selection(string='Tipo', selection=[('LT', 'Laptop'), ('DT', 'escritorio'), ('TA', 'tablet'), ('SP', 'smartphone')], default='LT')
    no_anydesk = fields.Integer(string='Numero anydesk')
    mac_address = fields.Char(string='Direccion MAC')
    barcode = fields.Char(string='Código', compute='_barcode', store=True)
    area_device = fields.Selection(string='Área', selection=[('P', 'produccion'), ('O', 'Oficinas'), ('M', 'Mesanin'), ('A', 'Almacen'), ('C', 'Comedor')], default='O')
    inventory_code = fields.Char(string='Código de inventario', compute='_inventory_code', store=True)
    so = fields.Selection(string='Sistema operativo', selection=[('W10', 'windows_10'), ('W8', 'windows_8'), ('W11', 'windows_11'), ('A', 'Android')])
    storage = fields.Integer(string='Almacenamiento', default=250)
    type_storage = fields.Selection(string='Tipo de almacenamiento', selection=[('SSD', "Estado solido"), ('HDD', "Disco mecanico")], default='SSD')
    description = fields.Html(string='Descripción')
    ram = fields.Selection(string='Tipo de memoria ram', selection=[('3', 'DDR3'), ('4', 'DDR4')], default="3")
    active = fields.Boolean(default=True,copy=True)
    


    @api.depends('type_device')
    def _inventory_code(self):
        for i in self:
            num = random.randint(111111, 999999)
            i.inventory_code = i.type_device + str(num)
        return i.inventory_code
    
    @api.depends('type_device')
    def _barcode(self):
        for i in self:
            num = random.randint(111111111111, 999999999999)
            i.barcode = str(num)
        return i.barcode

    
    def _status(self):
        pass

