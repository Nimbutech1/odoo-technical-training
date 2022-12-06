# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    member_id = fields.Many2one(comodel_name="space_mission.members", string="Related member", ondelete="set null")
    
    student_ids = fields.Many2one(string="Students", related="session_id.student_ids")
    