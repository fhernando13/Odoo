# -*- coding: utf-8 -*-
from odoo import http

# class MyBank(http.Controller):
#     @http.route('/my_bank/my_bank/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_bank/my_bank/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_bank.listing', {
#             'root': '/my_bank/my_bank',
#             'objects': http.request.env['my_bank.my_bank'].search([]),
#         })

#     @http.route('/my_bank/my_bank/objects/<model("my_bank.my_bank"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_bank.object', {
#             'object': obj
#         })