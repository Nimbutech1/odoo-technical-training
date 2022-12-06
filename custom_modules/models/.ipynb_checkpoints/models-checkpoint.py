# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Partnet(models.Model):
    _inherit = 'res.partner'
    
    image = fields.Binary(string="Image", attachment=True)
    
    def default_image(self, context=None):
        return 'static/img/image.jpg'
    
    # Set the default image for res_partner
    res_partner_default_image = fields.Binary('Default Image', attachment=True, default=lambda self: self._get_default_image())

    def _get_default_image(self):
        image_path = 'path/to/default/image.png'
        return open(image_path, 'rb').read()


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
