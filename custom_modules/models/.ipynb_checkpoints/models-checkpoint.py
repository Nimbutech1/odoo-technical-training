# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo import tools
from odoo.modules import get_module_resource
import base64

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
     def _avatar_get_placeholder_path(self):
            print(self)
        if self.is_company:
            return "custom_modules/static/img/image.jpg"
        if self.type == 'delivery':
            return "custom_modules/static/img/image.jpg"
        if self.type == 'invoice':
            return "custom_modules/static/img/image.jpg"
        return super()._avatar_get_placeholder_path()
    
class AvatarMixin(models.AbstractModel):
    _inherit = 'avatar.mixin'
    
     def _avatar_get_placeholder_path(self):
        return "custom_modules/static/img/avatar_grey.png"

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
