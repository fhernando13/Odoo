# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ti_support_brand(models.Model):
    _name = 'ti_support.ti_support_brand'

    name = fields.Char(string='Marca')
    
