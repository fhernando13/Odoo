# -*- coding: utf-8 -*-
from odoo import http

# class Comedor(http.Controller):
#     @http.route('/comedor/comedor/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/comedor/comedor/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('comedor.listing', {
#             'root': '/comedor/comedor',
#             'objects': http.request.env['comedor.comedor'].search([]),
#         })

#     @http.route('/comedor/comedor/objects/<model("comedor.comedor"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('comedor.object', {
#             'object': obj
#         })