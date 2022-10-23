# -*- coding: utf-8 -*-


from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ti_support_system(models.Model):
    _name = 'ti_support.ti_support_system'

    created_by = fields.Many2one(
        'res.users', 'Usuario', readonly=True, ondelete='restrict',
        default=lambda self: self.env.user,
        help="El ticket fue creado por el usuario", copy=False)
    no_payroll = fields.Integer(string='Número de nomina', require=True)
    no_phone = fields.Char(string='Número de telefono', require=True)
    email = fields.Char(string='Email 4G', require=True)
    area  = fields.Char(string='Área')
    state = fields.Selection(selection=[('p', 'Pendiente'), 
                                        ('e', 'En proceso'), 
                                        ('d', 'Terminado'), 
                                        ('c', 'Cancelado')], string='Estado', default="p")
    type_system = fields.Selection(selection=[('W', 'Windows'), 
                                              ('A', 'Android'), 
                                              ('O', 'Odoo')], string='Sistema', default="O")
    link_page = fields.Char(string='Link', require=True)
    issue = fields.Text(string='Descripcion del problema', require=True)
    caption  = fields.Html(string='Captura del error', require=True)
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

    def action_py(self):
        raise ValidationError("Esto es una prueba")

    # xml_file_name ='Nombre'+'.xml'
                # self.env['ir.attachment'].sudo().create(
                #                             {
                #                                 'name': xml_file_name,
                #                                 'datas': json_response['pago_xml'],
                #                                 'datas_fname': xml_file_name,
                #                                 'res_model': self._name,
                #                                 'res_id': p.id,
                #                                 'type': 'binary'
                #                             }