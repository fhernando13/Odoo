# -*- coding: utf-8 -*-

from odoo import models, fields, api
import random
from odoo.exceptions import ValidationError


class ti_support_device(models.Model):
    _name = 'ti_support.ti_support_device'


    name = fields.Char(string='Número de serie', required=True, help='Número de serie')
    name_id = fields.Many2one(comodel_name='ti_support.ti_support_model', string='Modelo')
    type_device = fields.Selection(string='Tipo', selection=[('LT', 'Laptop'), ('DT', 'escritorio'), ('TA', 'tablet'), ('SP', 'smartphone')], default='LT')
    mac_address = fields.Char(string='Direccion MAC', required=True, help="Número de 12 digitos hexadecimal")
    so = fields.Selection(string='Sistema operativo', selection=[('W10', 'windows 10'), ('W8', 'windows 8'), ('W11', 'windows 11'), ('A', 'Android')], default='W11', help='Sistema operativo del dispositivo')
    storage = fields.Integer(string='Almacenamiento', default=250, required=True, help='Espacio en disco')
    type_storage = fields.Selection(string='Tipo de almacenamiento', selection=[('SSD', "Estado solido"), ('HDD', "Disco mecanico"), ('HB', "Almacenamiento Hibrido")], default='SSD', help='Tipo de disco')
    ram = fields.Selection(string='Tipo de memoria ram', selection=[('3', 'DDR3'), ('4', 'DDR4')], default="3", help='Tipo de memoria ram')
    size_ram = fields.Integer('Tamaño de memoria ram', required=True, default=8, help='Tamaño de la memora ram en GB')
    active = fields.Boolean(default=True,copy=True)
    description = fields.Html(string='Descripción', required=True, help='Descripcion fisica del equipo')
    
   
   
    @api.depends('type_device')
    def _inventory_code(self):
        for i in self:
            num = random.randint(111111, 999999)
            i.name = i.type_device + str(num)
        return i.name


    @api.depends('type_device')
    def _barcode(self):
        for i in self:
            num = random.randint(111111111111, 999999999999)
            i.barcode = str(num)
        return i.barcode


    @api.constrains('mac_address')
    def check_macaddress(self):
        for i in self:
            if len(i.mac_address) != 12:
                raise ValidationError("El mac address %s no es de 12 digitos" % i.mac_address)


    @api.constrains('mac_address')
    def check_mac_address(self):
        for rec in self:
            mac_address = self.env['ti_support.ti_support_device'].search([('mac_address', '=', rec.mac_address), ('id', '!=', rec.id)])
            if mac_address:
                raise ValidationError("La mac address %s, ya existe!!!" % rec.mac_address)

    #generar un codigo aleatorio
    @api.constrains('barcode')
    def check_barcode(self):
        for rec in self:
            barcode = self.env['ti_support.ti_support_device'].search([('barcode', '=', rec.barcode), ('id', '!=', rec.id)])
            if barcode:
                raise ValidationError("La código %s, ya existe!!!" % rec.barcode)

    #Verificar el numeor de serie
    @api.constrains('name')
    def check_inventory_code(self):
        for rec in self:
            name = self.env['ti_support.ti_support_device'].search([('name', '=', rec.name), ('id', '!=', rec.id)])
            if name:
                raise ValidationError("El número de serie %s, ya existe!!!" % rec.name)