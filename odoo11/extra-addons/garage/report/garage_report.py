from odoo import _, api, fields, models


class GarageReportFull(models.Model):
    _name = 'garage.report_full'
    _description = 'Garage Full Report'
    _inherit = 'garage.moto'
    def _get_report(self):
        pass


class GarageReportCustom(models.Model):
    _name = 'garage.report_custom'
    _description = 'Garage Custom Report'
    name = fields.Char(string='Modelo', required=True)
    marca = fields.Char(string='Marca', required=True)
    matricula = fields.Char(string='Matricula', required=True)
    version = fields.Selection(string='Versión', selection=[('s', 'standard')], default='s')
    construido = fields.Date(string='Fecha de construccion', required=True)
    color = fields.Char(string='Color', required=True)
    precio = fields.Integer(string='Precio')
    def _get_report(self):
        pass

    
        
class GarageReportRecords(models.Model):
    _name = 'garage.report_records'
    _description = 'Garage Get Records Report'
    def _get_report(self):
        pass    

    
