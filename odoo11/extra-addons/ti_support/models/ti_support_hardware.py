# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ti_support_hardware(models.Model):
    _name = 'ti_support.ti_support_hardware'
    

    created_by = fields.Many2one(
        'res.users', 'Usuario', readonly=True, ondelete='restrict',
        default=lambda self: self.env.user,
        help="El ticket fue creado por el usuario", copy=False)
    no_payroll = fields.Integer(string='Número de nomina', required=True)
    no_phone = fields.Char(string='Número de telefono', required=True)
    email = fields.Char('Email', help="Email del usuario", required=True)
    area  = fields.Char(string='Área', required=True)
    state = fields.Selection(selection=[('p', 'Pendiente'), 
                                        ('i', 'En proceso'), 
                                        ('d', 'Terminado'), 
                                        ('c', 'Cancelado')], string='Estado', default="p")
    issue  = fields.Html(string='Descripcion del problema', require=True)
    progress = fields.Integer(string="Progreso", compute='_progress')
    date_created = fields.Datetime(
        'Hora', default=fields.Datetime.now, readonly=True, copy=False)
    

    @api.depends('state')
    def _progress(self):
        for rec in self:
            if rec.state == 'p':
                rec.progress = 0
            elif rec.state == 'i':
                rec.progress = 50
            elif rec.state == 'd':
                rec.progress = 100
            else:
                rec.state == 0

    @api.constrains('email')
    def _check_mail(self):
        for rec in self:
            email = self.env['res.users'].search([('login', '=', rec.email),  ('id', '!=', rec.id)])
            if not email:
                print('no existe')
                raise ValidationError("El email, no existe!!!")
    
    def change_state(self):
        if self.env.uid == True:
            if self.state == 'p':
                self.state = 'i'
            elif self.state == 'i':
                self.state = 'd'
            elif self.state == 'd':
                self.state = 'c'
            elif self.state == 'c':
                self.state = 'p'
        else:
            raise ValidationError("No tiene permisos para cambiar el estado del proceso!!")