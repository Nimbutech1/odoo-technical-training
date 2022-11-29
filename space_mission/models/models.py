# -*- coding: utf-8 -*-

from odoo import models, fields, api

class spacecraft(models.Model):
    _name = 'space_mission.spacecraft'
    
    size = fields.Integer(string='Dimensiones')
    shipType = fields.Selection(string='Tipo de nave',
                               selection=[('espacial','Espacial'),
                                          ('astronomica','Astronomica')])
    fuelType = fields.Selection(string='Tipo de combustible',
                               selection=[('gas','Gas'),
                                          ('electricidad','Electricidad'), 
                                          ('eolica','eolica')])
    passengersCont = fields.Integer('Numero de pasajeros')
    active = fields.Boolean(string='Activo', default=True)
    
    
# class space_mission(models.Model):
#     _name = 'space_mission.space_mission'
#     _description = 'space_mission.space_mission'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
