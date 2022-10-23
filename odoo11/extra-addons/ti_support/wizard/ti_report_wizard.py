from odoo import _, api, fields, models

#No se Guarda ;v
class ti_report_wizard(models.TransientModel):
    _name = 'ti_support.ti_report_wizard'
    _description = 'Wizard de Reporte de sistemas'

    email_select = fields.Selection('_get_email',string='E-mail',store=True) 
    area_select = fields.Selection('_get_area',string='Área',store=True) 
    state_select = fields.Selection('_get_state',string='Estado',store=True)
    
    
    def _get_email(self):
        selection = []
        records = self.env['ti_support.ti_support_hardware'].read_group([], fields=['email'], groupby=['email'])
        for rec in records:
            # ('val,key')
            val = (rec['email_count'],rec['name'])
            selection.append(val)        
        return selection

    def _get_area(self):
        selection = []
        records = self.env['ti_support.ti_support_hardware'].read_group([], fields=['area'], groupby=['area'])
        for rec in records:
            # ('val,key')
            val = (rec['area_count'],rec['area'])
            selection.append(val)        
        return selection       

    def _get_state(self):
        selection = []
        records = self.env['ti_support.ti_support_hardware'].read_group([], fields=['state'], groupby=['state'])
        for rec in records:
            # ('val,key')
            val = (rec['state_count'],rec['state'])
            selection.append(val)        
        return selection     

    def field_view_get(self, view_id=None, view_type='form', toolbal=False, submenu=False):
        device = super(ti_report_wizard, self).fields_view_get(view_id=view_id, view_type=view_type, toolbal=toolbal, submenu=submenu)
        return device

    
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