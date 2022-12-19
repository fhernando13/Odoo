# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
from email.message import EmailMessage 
import smtplib 
from email.message import EmailMessage 

class ti_support_technical_support(models.Model):
    _name = 'ti_support.ti_support_technical_support'
    _inherit = 'mail.thread'
    _rec_name = 'name'

    name = fields.Char(string='No. ticket', default=lambda self: self.env['ir.sequence'].next_by_code('ti_support.ti_support_technical_support'))
    created_by = fields.Many2one(
        'res.users', 'Usuario', readonly=True, ondelete='restrict',
        default=lambda self: self.env.user,
        help="El ticket fue creado por el usuario", copy=False)
    area  = fields.Char(string='Área')
    state = fields.Selection(selection=[('p', 'Pendiente'), 
                                        ('i', 'En proceso'), 
                                        ('d', 'Terminado'), 
                                        ('c', 'Cancelado')], string='Estado', default="p")
    type_error = fields.Selection(selection=[('W', 'Windows'), 
                                              ('A', 'Android'), 
                                              ('O', 'Odoo'),
                                              ('R', 'Red'),
                                              ('E', 'Equipos'),
                                              ('I', 'Impresora'),
                                              ('Os', 'Otro')], string='Sistema', default="O")
    link_page = fields.Char(string='Link', require=True)
    issue = fields.Text(string='Descripcion del problema', require=True)
    caption  = fields.Html(string='Captura del error', require=True)
    progress = fields.Integer(string="Progreso", compute='_progress')
    date_created = fields.Datetime('Hora', default=fields.Datetime.now, readonly=True, copy=False)
    
    
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
                raise UserError("El email, no existe!!!")

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
            raise UserError("No tiene permisos para cambiar el estado del proceso!!")
    

    def mail(self):
        e = self.env.user.email
        return e


    @api.model
    def create(self,values):
        #enviar email al crear ticket
        u = self.env.user.name
        e = self.mail()
        email_subject = "Ticket de soporte técnico" 
        sender_email_address =  "erp@4gingenieria.com"
        receiver_email_address = "josep@4gingenieria.com"
        #another_email_address = "moisesq@gingenieria.com"

        email_smtp = "mail.4gingenieria.com" 
        email_password = "Gacl751001E85"

        message = EmailMessage() 
        message['Subject'] = email_subject 
        message['From'] = sender_email_address 
        message['To'] = receiver_email_address 
        #message['CC'] = another_email_address
        message.set_content("Se ha creado un tecket de soporte tecnico por el usuario: " + u + ", con correo: " + e) 
        server = smtplib.SMTP(email_smtp, '587') 
        server.ehlo() 
        server.starttls() 
        server.login(sender_email_address, email_password) 
        server.send_message(message) 
        server.quit()
        override_create = super(ti_support_technical_support,self).create(values)
        return override_create
