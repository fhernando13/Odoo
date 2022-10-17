# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime


class ti_support_assignment(models.Model):
    _name = 'ti_support.ti_support_assignment'  


    date_assignment = fields.Date(string='Fecha de asignacion', require=True)
    status = fields.Selection(string='Estado', selection=[('N', 'Nuevo'), ('U', 'Usado')], default='N', require=True)
    employee_id = fields.Char(string='Empleado', require=True)
    device_id = fields.Many2one('ti_support.ti_support_device', string='Dispositivo', require=True) 
    time_assignment = fields.Integer(string='Días con el equipo', compute='time_trans')
    condition = fields.Selection(selection=[('p', 'Prestado'), ('a', 'Asignado')], default='a', require=True)

    @api.multi
    def time_trans(self):
        for record in self:
            today = datetime.date.today()
            today2 = record.date_assignment
            today2 = str(today2)
            year = today2[0:4]
            month = today2[5:7]
            day = today2[8:10]
            someday = datetime.date(int(year), int(month), int(day))
            if someday == today:
                record.time_assignment = 0
            else:
                difDays = someday - today
                difDays = str(difDays)
                difDays = difDays[1:]
                days = ''
                for i in difDays:
                    if i.isdigit():
                        days = days+i
                        continue
                    else:
                        break
            record.time_assignment = days


   