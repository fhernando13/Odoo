# -*- coding: utf-8 -*-

from odoo import models, fields, api


class registro_moto(models.Model):
    _name = 'garage.registro_moto'
    _description = 'Registro de motocicletas'
    
    employee_id = fields.Many2one('res.partner', string='Usuario', ondelete='cascade', required=True, help="Dueño de la moto")
    name_id = fields.Many2one('garage.modelo_moto', string='Modelo', ondelete='cascade', requiered=True)
    matricula = fields.Char(string='Matricula', required=True, help="Matricula de la motocicleta")
    codigo = fields.Char(string='Código', required=True)
    descripcion = fields.Text(string='Descripción', required=True, help="Descripción física de la motocicleta")
    

    #relaciones
    estacionamiento_id = fields.Many2one('garage.estacionamiento', string = 'Estacionamiento')
    estacionamiento_ids = fields.Many2many('garage.estacionamiento', string = 'Mantenimiento')

    @api.model
    def create(self, values):    
        result = super(registro_moto, self).create(values)
        return result
    