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

class auto(models.Model):
    _name = 'garaje.auto'
    _description = 'Permite definir las caracteriticas de un auto'
    _order = 'name'
    
    name = fields.Char(string='Matricula', required=True)
    modelo = fields.Char(string='Modelo', required=True)
    construido = fields.Date(string='Fecha de construccion', required=True)
    consumo = fields.Float('Consumo', (4,1), default=0.0, help='Consumo promedio')
    descompuesto = fields.Boolean(string='Descompuesto', default=False)
    #store=True
    year = fields.Integer(string = 'Años', compute ='_get_year', store=True)
    descripcion = fields.Text('Descripcion')

    #relaciones
    estacionamiento_id = fields.Many2one('garaje.estacionamiento', string = 'Estacionamiento')
    estacionamiento_ids = fields.Many2many('garaje.estacionamiento', string = 'Mantenimiento')
    
    
    @api.depends('construido')
    def get_year(self):
        for auto in self:
            hoy = date.today()
            auto.year = relativedelta(hoy, auto.construido).years
    
    #restricciones formato bbdd
    #sql_constrains = [('name_unique', 'unique(name)','la matricula ya existe')]

class mantenimiento(models.Model):
    _name = 'garaje.mantenimiento'
    _description = 'Permite definir las caracteriticas del mantenimiento'
    _order = 'fecha'
    
    fecha = fields.Date(string = 'Fecha', required = True, default = fields.date.today())
    tipo = fields.Selection(string = 'Tipo', selection = [('l','lavar'), ('m','mecanica'), ('p','pintura')], default='l')
    costo = fields.Float('Costo', (8,2), help = 'Costo de mantenimiento')

    #relaciones
    auto_ids =  fields.Many2many('garaje.auto', string='Autos')

    # def get_name(self):
    #     resultados = []
    #     for mantenimiento in self:
    #         descripcion = f'{len(mantenimiento.auto_ids), autos - {mantenimiento.coste}} €'
    #         resultados.append(mantenimiento.id, descripcion)
    #     return resultados