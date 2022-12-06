# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo import tools
from odoo.modules import get_module_resource
import base64

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    def _get_default_image(self):
        image_path = modules.get_module_resource('custom_modules', 'static/img', 'image.jpg')
        return tools.image_resize_image_big(base64.b64encode(open(image_path, 'rb').read()))
    
    image = fields.Binary("Photo", default='_get_default_image')
    image_1920 = = fields.Binary("Photo", default='_get_default_image')
    

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
