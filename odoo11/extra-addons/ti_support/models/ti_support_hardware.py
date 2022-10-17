# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ti_support_hardware(models.Model):
    _name = 'ti_support.ti_support_hardware'

    name = fields.Char(string='Empleado', require=True)
    no_payroll = fields.Integer(string='Número de nomina', require=True)
    no_phone = fields.Char(string='Número de telefono')
    email = fields.Char(string='Direccion de correo electronico 4G', require=True)
    area  = fields.Char(string='Área')
    state = fields.Selection(selection=[('p', 'Pendiente'), 
                                        ('e', 'En proceso'), 
                                        ('d', 'Terminado'), 
                                        ('c', 'Cancelado')], string='Estado', default="p")
    issue  = fields.Html(string='Descripcion del problema', require=True)
    progress = fields.Integer(string="Progreso", compute='_progress')
    

    @api.depends('state')
    def _progress(self):
        for rec in self:
            if rec.state == 'p':
                rec.progress = 0
            elif rec.state == 'e':
                rec.progress = 50
            elif rec.state == 'd':
                rec.progress = 100
            else:
                rec.state == 0
                