# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ti_support_hardware(models.Model):
    _name = 'ti_support.ti_support_hardware'
    

    created_by = fields.Many2one(
        'res.users', 'Usuario', readonly=True, ondelete='restrict',
        default=lambda self: self.env.user,
        help="El ticket fue creado por el usuario", copy=False)
    no_payroll = fields.Integer(string='Número de nomina', require=True)
    no_phone = fields.Char(string='Número de telefono', require=True)
    email = fields.Char('Email', help="Email del usuario", require=True)
    area  = fields.Char(string='Área', require=True)
    state = fields.Selection(selection=[('p', 'Pendiente'), 
                                        ('e', 'En proceso'), 
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
            elif rec.state == 'e':
                rec.progress = 50
            elif rec.state == 'd':
                rec.progress = 100
            else:
                rec.state == 0

    @api.constrains('email')
    def _check_mail(self):
        for rec in self:
            email = self.env['hr.employee'].search([('work_email', '=', rec.email),  ('id', '!=', rec.id)])
            if not email:
                print('no existe')
                raise ValidationError("El email, no existe!!!")