# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import *
from datetime import date


class moto(models.Model):
    _name = 'garaje.moto'
    _description = 'Permite definir las caracteriticas de una motocicleta'
    _order = 'name'
    
    name = fields.Char(string='Modelo', required=True)
    marca = fields.Char(string='Marca', required=True)
    matricula = fields.Char(string='Matricula', required=True)
    version = fields.Selection(string='Versión', selection=[('s', 'standard')], default='s')
    tipo = fields.Selection(string='Tipo', selection=[('t', 'trabajo'), ('c', 'ciudad'), ('d', 'deportiva')])
    construido = fields.Date(string='Fecha de construccion', required=True)
    consumo = fields.Float('Consumo', (4,1), default=0.0, help='Consumo x km')
    motor = fields.Integer(string='C.C. motor', required=True, help='Tamaño del motor')
    color = fields.Char(string='Color', required=True)
    precio = fields.Integer(string='Precio')
    descripcion = fields.Html('Descripcion')

    #relaciones
    estacionamiento_id = fields.Many2one('garaje.estacionamiento', string = 'Estacionamiento')
    estacionamiento_ids = fields.Many2many('garaje.estacionamiento', string = 'Mantenimiento')

    @api.model
    def create(self, values):    
        result = super(moto, self).create(values)
        return result
    