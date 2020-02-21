# -*- coding: utf-8 -*-
# from odoo import http


# class Entretamiento(http.Controller):
#     @http.route('/entretamiento/entretamiento/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/entretamiento/entretamiento/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('entretamiento.listing', {
#             'root': '/entretamiento/entretamiento',
#             'objects': http.request.env['entretamiento.entretamiento'].search([]),
#         })

#     @http.route('/entretamiento/entretamiento/objects/<model("entretamiento.entretamiento"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('entretamiento.object', {
#             'object': obj
#         })
