# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import *
from datetime import date


class auto(models.Model):
    _name = 'garage.auto'
    _description = 'Permite definir las caracteriticas de un auto'
    _order = 'name'
    
    name = fields.Char(string='Modelo', required=True)
    marca = fields.Char(string='Marca', required=True)
    matricula = fields.Char(string='Matricula', required=True)
    version = fields.Selection(string='Versión', selection=[('s', 'standard'), ('a', 'automatico')], default='s')
    tipo = fields.Selection(string='Tipo', selection=[('p', 'pickup'),('s', 'sedan'), ('l', 'lujo'), ('d', 'deportivo')], default='s')
    construido = fields.Date(string='Año', required=True)
    consumo = fields.Float('Consumo', (4,1), default=0.0, help='Consumo x km')
    motor = fields.Integer(string='C.C. motor', required=True, help='Tamaño del motor')
    color = fields.Char(string='Color', required=True)
    precio = fields.Integer(string='Precio')
    descripcion = fields.Html('Descripcion')

    #relaciones
    estacionamiento_id = fields.Many2one('garage.estacionamiento', string = 'Estacionamiento')
    estacionamiento_ids = fields.Many2many('garage.estacionamiento', string = 'Mantenimiento')

    @api.model
    def create(self, values):    
        result = super(auto, self).create(values)
        return result
    