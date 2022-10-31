from odoo import _, api, fields, models

#No se Guarda ;v
class report(models.Model):
    _name = 'garage.report'

    @api.multi
    def get_report(self):
        action = self.env.ref('garage.moto_action_window').read()[0]
        action['domain'] = [('name', '=', 'ax100'),('marca', '=', 'Susuki'), ('color', '!=', 'negro')]
        return action
    

    
    def get_report2(self):
        action = self.env['garage.registro_moto'].search([])
        for act in action:
            for x in act:
                print(x.name, x.marca)


    #example
    def temp_posting(self, cr, uid, ids, context=None):
        tea_v = {}
        tea_list_data = []

        if context is None:
            context = {}
        bpl_division_id = context['bpl_division_id']
        work_update_ids = self.pool.get('bpl.work.update').search(cr, uid, [('bpl_division_id', '=', bpl_division_id)])
        work_update_obj = self.pool.get('bpl.work.update').browse(cr, uid, work_update_ids)[0]
        if work_update_obj:
            work_update_obj.write({'state': 'negotiation'})        

        for record in work_update_obj.selected_tea_workers_update_line_ids:
            tea_list_data.append({'bpl_company_id': record.work_id.bpl_company_id.id, 'bpl_estate_id': record.work_id.bpl_estate_id.id, 'bpl_division_id': record.work_id.bpl_division_id.id, 'worker_id': record.worker_id.id, 'date': record.work_id.offered_date, 'type':'tea', 'names': 6.00, 'output':record.tea_total_kgs, 'over_kgs':2, 'scrap':3, 'pss':30.00})
        for record in work_update_obj.selected_rubber_workers_update_line_ids:
            tea_list_data.append({'bpl_company_id': record.work_id.bpl_company_id.id, 'bpl_estate_id': record.work_id.bpl_estate_id.id, 'bpl_division_id': record.work_id.bpl_division_id.id, 'worker_id': record.worker_id.id, 'date': record.work_id.offered_date, 'type':'rubber', 'names': 6.00, 'output':record.rubber_total_kgs, 'over_kgs':2, 'scrap':3, 'pss':30.00})    
        for record in work_update_obj.selected_sundry_workers_update_line_ids:
            tea_list_data.append({'bpl_company_id': record.work_id.bpl_company_id.id, 'bpl_estate_id': record.work_id.bpl_estate_id.id, 'bpl_division_id': record.work_id.bpl_division_id.id, 'worker_id': record.worker_id.id, 'date': record.work_id.offered_date, 'type':'sundry', 'names':record.sundry_hrs_worked, })    
        for record in work_update_obj.selected_other_workers_update_line_ids:
            tea_list_data.append({'bpl_company_id': record.work_id.bpl_company_id.id, 'bpl_estate_id': record.work_id.bpl_estate_id.id, 'bpl_division_id': record.work_id.bpl_division_id.id, 'worker_id': record.worker_id.id, 'date': record.work_id.offered_date, })
        #tea_v = {tea_list_data} line remove

        daily_transaction_master = self.pool.get('bpl.daily.transaction.master')
        #daily_transaction_master.create(cr, uid, tea_v, context=context)
        for record in tea_list_data:
            daily_transaction_master.create(cr, uid, record, context=context)
        return True