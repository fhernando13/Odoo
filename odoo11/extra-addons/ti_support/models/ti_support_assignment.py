# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime
from odoo.exceptions import ValidationError


class ti_support_assignment(models.Model):
    _name = 'ti_support.ti_support_assignment'

    
    name = fields.Many2one('hr.employee', string='Empleado', required=True, help='A quién se le asignará el dispostivo')
    name_id = fields.Many2one('ti_support.ti_support_device', string='Dispositivo', required=True)
    date_assignment = fields.Date(string='Fecha de asignacion', required=True)
    status = fields.Selection(string='Estado', selection=[('N', 'Nuevo'), ('U', 'Usado')], default='N', require=True)
    time_assignment = fields.Integer(string='Días con el equipo', compute='time_trans')
    condition = fields.Selection(selection=[('p', 'Prestado'), ('a', 'Asignado')], default='a', required=True)
    area_device = fields.Selection(string='Área', selection=[('P', 'produccion'), ('O', 'Oficinas'), ('M', 'Mesanin'), ('A', 'Almacen'), ('C', 'Comedor')], default='O')
    no_anydesk = fields.Char(string='Numero anydesk', required=True, help="Número de 9 digitos decimal")


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

    @api.constrains('no_anydesk')
    def check_anydesk(self):
        for i in self:
            if len(i.no_anydesk) != 9:
                raise ValidationError("El numero %s no es de 9 digitos" % i.no_anydesk)


    @api.constrains('no_anydesk')
    def check_no_anydesk(self):
        for rec in self:
            anydesk = self.env['ti_support.ti_support_assignment'].search([('no_anydesk', '=', rec.no_anydesk), ('id', '!=', rec.id)])
            if anydesk:
                raise ValidationError("El número %s anydesk, ya existe!!!" % rec.no_anydesk)




