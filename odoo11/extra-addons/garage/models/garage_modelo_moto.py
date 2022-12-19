# -*- coding: utf-8 -*-

from odoo import models, fields, api


class modelo_moto(models.Model):
    _name = 'garage.modelo_moto'
    _description = 'Registro de modelos de motocicletas'
    _order='name'
    
    
    name = fields.Char(string='Modelo', required=True)
    name_id = fields.Many2one('garage.marca_moto', string="Marca", help="Marca de la motocicleta")
    velocidades = fields.Selection(string='Velocidades', selection=[('5', 'Cinco'), ('6', 'Seis')], default='5', help="Velocidades")
    tipo = fields.Selection(string='Tipo', selection=[('t', 'trabajo'), ('c', 'ciudad'), ('d', 'deportiva')], default='c')
    anio = fields.Integer(string='Año', required=True, help="Año de construccion")
    consumo = fields.Float('Rendimiento', (4,1), default=0.0, required=True,  help='Consumo de gasolina x km')
    motor = fields.Integer(string='C.C. motor', help='Cilindrada del motor', required=True)
    color = fields.Char(string='Color', required=True, help='Color de la motocicleta')
