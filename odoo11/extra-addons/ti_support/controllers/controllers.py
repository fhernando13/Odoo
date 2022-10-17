# -*- coding: utf-8 -*-
from odoo import http

# class TiSupport(http.Controller):
#     @http.route('/ti_support/ti_support/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ti_support/ti_support/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ti_support.listing', {
#             'root': '/ti_support/ti_support',
#             'objects': http.request.env['ti_support.ti_support'].search([]),
#         })

#     @http.route('/ti_support/ti_support/objects/<model("ti_support.ti_support"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ti_support.object', {
#             'object': obj
#         })