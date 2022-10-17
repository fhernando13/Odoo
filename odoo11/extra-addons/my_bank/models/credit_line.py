# -*- coding: utf-8 -*-

from odoo import models, fields, api

class credit_line(models.Model):
    _name = 'my_bank.credit_line'

    date_line_credit = fields.Date(string='Fecha linea de credito', required=True)
    name = fields.Char(string="Nombre linea de credito", required=True)
    required_amount = fields.Integer(string="Monto requerido", required=True)
