# -*- coding: utf-8 -*-
from odoo import models, fields, api
from dateutil.relativedelta import *
from datetime import date

class estacionamiento(models.Model):
    _name = 'garaje.estacionamiento'
    _description = 'Permite definir las caracteriticas de un estacionamiento'
    
    name = fields.Char(string = 'Direccion', required=True)
    plazas = fields.Integer(string='Plazas', Required=True)

    #relaciones
    auto_ids = fields.One2many('garaje.auto', 'estacionamiento_id', string = 'Autos')
    moto_ids = fields.One2many('garaje.moto', 'estacionamiento_id', string = 'Motos')