# -*- coding: utf-8 -*-


from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ti_support_system(models.Model):
    _name = 'ti_support.ti_support_system'

    name = fields.Char(string='Nombre', require=True)
    no_payroll = fields.Integer(string='Número de nomina', require=True)
    no_phone = fields.Char(string='Número de telefono')
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
    caption  = fields.Binary(string='captura del error', require=True)
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