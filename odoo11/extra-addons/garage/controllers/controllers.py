# -*- coding: utf-8 -*-
from odoo import http

# class Garage(http.Controller):
#     @http.route('/garage/garage/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/garage/garage/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('garage.listing', {
#             'root': '/garage/garage',
#             'objects': http.request.env['garage.garage'].search([]),
#         })

#     @http.route('/garage/garage/objects/<model("garage.garage"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('garage.object', {
#             'object': obj
#         })