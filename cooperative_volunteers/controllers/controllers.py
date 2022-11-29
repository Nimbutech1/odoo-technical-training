# -*- coding: utf-8 -*-
# from odoo import http


# class CooperativeVolunteers(http.Controller):
#     @http.route('/cooperative_volunteers/cooperative_volunteers', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cooperative_volunteers/cooperative_volunteers/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cooperative_volunteers.listing', {
#             'root': '/cooperative_volunteers/cooperative_volunteers',
#             'objects': http.request.env['cooperative_volunteers.cooperative_volunteers'].search([]),
#         })

#     @http.route('/cooperative_volunteers/cooperative_volunteers/objects/<model("cooperative_volunteers.cooperative_volunteers"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cooperative_volunteers.object', {
#             'object': obj
#         })
