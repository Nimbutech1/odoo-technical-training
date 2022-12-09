# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    def _avatar_get_placeholder_path(self):
        if self.is_company:
            return "custom_modules/static/img/custom_company.png"
        if self.type == 'delivery':
            return "base/static/img/truck.png"
        if self.type == 'invoice':
            return "base/static/img/money.png"
        return super()._avatar_get_placeholder_path()
    
class AvatarMixin(models.AbstractModel):
    _inherit = avatar.mixin
    
    def _avatar_get_placeholder_path(self):
        return "custom_modules/static/img/custom_user.png"
    
# class custom_modules(models.Model):
#     _name = 'custom_modules.custom_modules'
#     _description = 'custom_modules.custom_modules'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
