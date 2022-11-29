# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Book(models.Model):
    _name = 'library_management.book'
    
    name = fields.Char(string="Nombre del libro")
    author_id = fields.Many2one(comodel_name="library_management.author", string="Autor")
    
class Author(models.Model):
    _name = 'library_management.author'
    
    name = fields.Char(string="Nombre del autor")
    age = fields.Integer(string="Edad del autor")

# class library_management(models.Model):
#     _name = 'library_management.library_management'
#     _description = 'library_management.library_management'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
