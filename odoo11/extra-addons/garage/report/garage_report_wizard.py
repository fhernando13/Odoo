from odoo import _, api, fields, models

#No se Guarda ;v
class ReportWizard(models.TransientModel):
    _name = 'garage.report_wizard'
    _description = 'Wizard de Reporte de Garage'


    model1 = fields.Selection('_get_model',string='Marca',store=True) 
    model2 = fields.Many2one('garage.moto', string='Marca2')
    
    model = fields.Char(string='Marca')
    fromdate = fields.Date('desde')
    todate = fields.Date('hasta')

    def _get_model(self):
        selection = []
        records = self.env['garage.moto'].read_group([], fields=['name'], groupby=['name'])
        for rec in records:
            # ('val,key')
            val = (rec['name_count'],rec['name'])
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


    def _get_marca(self):
        selection = []
        records = self.env['garage.moto'].read_group([], fields=['marca'], groupby=['marca'])
        for rec in records:
            # ('val,key')
            val = (rec['marca_count'],rec['marca'])
            selection.append(val)
        return selection

    @api.multi
    def get_report(self):
        print('mi modelo',self.model1)
        action = self.env['garage.moto'].search([('name', '=', self.model), ('construido', '<', self.todate)]).sorted('construido')
        print(action)
        for act in action:
            for i in act:
                print(i.name)
        
        
        
        # 
        # return action



    # def _get_marca(self):
    #     selection = []
    #     records = self.env['garage.moto'].read_group([], fields=['marca'], groupby=['marca'])
    #     for rec in records:
    #         # ('val,key')
    #         val = (rec['marca_count'],rec['marca'])
    #         selection.append(val)
    #     return selection

    # # def _get_motor(self):
    # #     selection = []
    # #     records = self.env['garage.moto'].read_group([], fields=['motor'], groupby=['motor'])
    # #     for rec in records:
    # #         # ('val,key')
    # #         val = (rec['motor_count'],rec['motor'])
    # #         selection.append(val)
    # #     return selection




    # def get_report(self):
    #     action = self.env.ref('garage.moto_action_window').read()[0]
    #     #action['domain'] = [('name', '=', self.name_select),('marca', '=', self.marca_select), ('color', '=', self.color_select)]
    #     print(action)
    #     return action



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