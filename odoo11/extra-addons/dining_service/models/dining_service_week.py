# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime

class dining_service_week(models.Model):
    _name = 'dining_service.dining_service_week'

    name = fields.Char(string='Semana', compute='week_iso')
    state = fields.Integer(string='Estado')

    def week_iso(self):
        date_today = datetime.date.today()
        number_week = date_today.isocalendar()
        number_day = date_today.isoweekday()
        if number_day > 3:
            number_week = str(number_week[1] + 1)
        else:
            number_week = str(number_week[1])
        return 'SEMANA '+str(number_week)

   