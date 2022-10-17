# -*- coding: utf-8 -*-

from odoo import models, fields, api

class balance_bank(models.Model):
    _name = 'my_bank.balance_bank'

    date_balance = fields.Date(string='Fecha', required=True)
    name = fields.Char(string="Nombre del banco")
    balance_today = fields.Integer(string="Saldo al día", required = True)
    
