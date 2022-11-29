# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Task(models.Model):
    _name = 'cooperative_volunteers.task'
    
    startTime = fields.Datetime(string="Hora de inicio")
    endTime = fields.Datetime(string="Hora de fin")
    name = fields.Char(string="Nombre de la tarea")
    description = fields.Text(string="Descripción de la tarea")
    taskType = fields.Selection(string="Tipo de tarea", selection=[('individual', 'Individual'),
                                                                   ('grupal','Grupal')])
    isRepeated = fields.Boolean(string="¿Se repite?")
    repetitions = fields.Integer(string="Repeticiones", compute='_compute_repetitions')
    
    def _compute_repititions(self):
        for record in self:
            record.repetitions += 1
    
    
# class cooperative_volunteers(models.Model):
#     _name = 'cooperative_volunteers.cooperative_volunteers'
#     _description = 'cooperative_volunteers.cooperative_volunteers'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
