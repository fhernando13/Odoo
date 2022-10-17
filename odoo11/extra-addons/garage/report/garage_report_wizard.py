from odoo import _, api, fields, models

#No se Guarda ;v
class ReportWizard(models.TransientModel):
    _name = 'garage.report_wizard'
    _description = 'Wizard de Reporte de Garage'

    marca_select = fields.Selection('_get_marca',string='Marca',store=True) 
    motor_select = fields.Selection('_get_motor',string='C.C. motor',store=True) 
    color_select = fields.Selection('_get_color',string='Color',store=True)
    precio_li = fields.Integer(string='Precio desde:',store=True)
    precio_ls = fields.Integer(string='Precio hasta:',store=True)
    name_select = fields.Selection('_get_name',string='Modelo',store=True)
    def _get_name(self):
        selection = []
        records = self.env['garage.moto'].read_group([], fields=['name'], groupby=['name'])
        for rec in records:
            # ('val,key')
            val = (rec['name_count'],rec['name'])
            selection.append(val)        
        return selection

    def _get_marca(self):
        selection = []
        records = self.env['garage.moto'].read_group([], fields=['marca'], groupby=['marca'])
        for rec in records:
            # ('val,key')
            val = (rec['marca_count'],rec['marca'])
            selection.append(val)        
        return selection       

    def _get_motor(self):
        selection = []
        records = self.env['garage.moto'].read_group([], fields=['motor'], groupby=['motor'])
        for rec in records:
            # ('val,key')
            val = (rec['motor_count'],rec['motor'])
            selection.append(val)        
        return selection     

    def _get_color(self):
        selection = []
        records = self.env['garage.moto'].read_group([], fields=['color'], groupby=['color'])
        for rec in records:
            # ('val,key')
            val = (rec['color_count'],rec['color'])
            selection.append(val)        
        return selection   

    def get_report(self,values):
        x = dict(self)
        print(x)


    
# Con @api.multi puedes retornar vistas como:
# return {
#     'name': _(' Human Readable String'),
#     'type': 'ir.actions.act_window',
#     'view_type': 'form',
#     'view_mode': 'tree,form',
#     'res_model': 'model',
#     'domain': [('id', 'in', ids)],
# }

# 1- Crear la acción de código
# 2- Definir el Método del reporte
# 3- Retornar la vista