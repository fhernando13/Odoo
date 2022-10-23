# -*- coding: utf-8 -*-

from odoo import models, fields, api
import random 
from odoo.exceptions import ValidationError


class ti_support_device(models.Model):
    _name = 'ti_support.ti_support_device'


    name = fields.Char(string='Modelo')
    brand_id = fields.Many2one('ti_support.ti_support_brand', string='Marca')  
    type_device = fields.Selection(string='Tipo', selection=[('LT', 'Laptop'), ('DT', 'escritorio'), ('TA', 'tablet'), ('SP', 'smartphone')], default='LT')
    no_anydesk = fields.Char(string='Numero anydesk', require=True)
    mac_address = fields.Char(string='Direccion MAC')
    barcode = fields.Char(string='Código', compute='_barcode', store=True)
    area_device = fields.Selection(string='Área', selection=[('P', 'produccion'), ('O', 'Oficinas'), ('M', 'Mesanin'), ('A', 'Almacen'), ('C', 'Comedor')], default='O')
    inventory_code = fields.Char(string='Código de inventario', compute='_inventory_code', store=True)
    so = fields.Selection(string='Sistema operativo', selection=[('W10', 'windows 10'), 
                                                                ('W8', 'windows 8'), 
                                                                ('W11', 'windows 11'), 
                                                                ('A', 'Android')])
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


    @api.constrains('no_anydesk')
    def check_anydesk(self):
        for i in self:
            if len(i.no_anydesk) != 9:
                raise ValidationError("El numero %s no es de 9 digitos" % i.no_anydesk)


    @api.constrains('no_anydesk')
    def check_no_anydesk(self):
        for rec in self:
            anydesk = self.env['ti_support.ti_support_device'].search([('no_anydesk', '=', rec.no_anydesk), ('id', '!=', rec.id)])
            if anydesk:
                raise ValidationError("El número %s anydesk, ya existe!!!" % rec.no_anydesk)
    

    @api.constrains('mac_address')
    def check_macaddress(self):
        for i in self:
            if len(i.mac_address) != 12:
                raise ValidationError("El mac address %s no es de 9 digitos" % i.mac_address)
    

    @api.constrains('mac_address')
    def check_mac_address(self):
        for rec in self:
            mac_address = self.env['ti_support.ti_support_device'].search([('mac_address', '=', rec.mac_address), ('id', '!=', rec.id)])
            if mac_address:
                raise ValidationError("La mac address %s, ya existe!!!" % rec.mac_address)


    @api.constrains('barcode')
    def check_barcode(self):
        for rec in self:
            barcode = self.env['ti_support.ti_support_device'].search([('barcode', '=', rec.barcode), ('id', '!=', rec.id)])
            if barcode:
                raise ValidationError("La código %s, ya existe!!!" % rec.barcode)
    

    @api.constrains('inventory_code')
    def check_inventory_code(self):
        for rec in self:
            inventory_code = self.env['ti_support.ti_support_device'].search([('inventory_code', '=', rec.inventory_code), ('id', '!=', rec.id)])
            if inventory_code:
                raise ValidationError("La código de inventario %s, ya existe!!!" % rec.inventory_code)