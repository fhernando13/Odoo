# -*- coding: utf-8 -*-
from odoo import models, fields, api
from dateutil.relativedelta import *
from datetime import date

class mantenimiento(models.Model):
    _name = 'garage.mantenimiento'
    _description = 'Permite definir las caracteriticas del mantenimiento'
    _order = 'fecha'
    
    fecha = fields.Date(string = 'Fecha', required = True, default = fields.date.today())
    tipo = fields.Selection(string = 'Tipo', selection = [('l','lavar'), ('m','mecanica'), ('p','pintura')], default='l')
    costo = fields.Float('Costo', (8,2), help = 'Costo de mantenimiento')

    #relaciones
    auto_ids =  fields.Many2many('garage.auto', string='Autos')
    moto_ids =  fields.Many2many('garage.registro_moto', string='Motos')

    # def get_name(self):
    #     resultados = []
    #     for mantenimiento in self:
    #         descripcion = f'{len(mantenimiento.auto_ids), autos - {mantenimiento.coste}} €'
    #         resultados.append(mantenimiento.id, descripcion)
    #     return resultados