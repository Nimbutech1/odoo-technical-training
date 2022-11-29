# -*- coding: utf-8 -*-
# from odoo import http


# class SpaceMission(http.Controller):
#     @http.route('/space_mission/space_mission', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/space_mission/space_mission/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('space_mission.listing', {
#             'root': '/space_mission/space_mission',
#             'objects': http.request.env['space_mission.space_mission'].search([]),
#         })

#     @http.route('/space_mission/space_mission/objects/<model("space_mission.space_mission"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('space_mission.object', {
#             'object': obj
#         })
