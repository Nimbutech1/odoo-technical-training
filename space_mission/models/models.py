# -*- coding: utf-8 -*-
from odoo import fields, models, api

class Spacecraft(models.Model):
    _name = 'space_mission.spacecraft'

    name = fields.Char()
    manufacturer = fields.Char()
    model = fields.Char()
    launch_date = fields.Date()
    weight = fields.Float()
    payload_capacity = fields.Float()
    
    active = fields.Boolean(string="Activo", default=True)

    # many2one field
    #Una nave espacial puede estar asociada a una o varias misiones
    mission_id = fields.Many2one(comodel_name='space_mission.mission', string='Mission')

    # one2many field
    crew = fields.One2many(comodel_name='space_mission.astronaut', inverse_name='spacecraft_id', string='Crew')


class Mission(models.Model):
    _name = 'space_mission.mission'

    name = fields.Char()
    launch_date = fields.Date()
    objective = fields.Text()
    budget = fields.Float()
    status = fields.Selection([
        ('planning', 'Planning'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ], default='planning')

    # many2one field
    # Una misión puede estar asociada a una nave espacial
    spacecraft_id = fields.Many2one(comodel_name='space_mission.spacecraft', string='Spacecraft', ondelete="cascade")

    # many2many field
    astronauts = fields.Many2many(comodel_name='space_mission.astronaut', relation='mission_astronaut_rel', column1='mission_id', column2='astronaut_id', string='Astronauts')

    # one2many field
    # Una mision puede tener una o varias fases
    phase_ids = fields.One2many(comodel_name='space_mission.mission_phase', inverse_name='mission_id', string='Phases')


class MissionPhase(models.Model):
    _name = 'space_mission.mission_phase'

    name = fields.Char()
    start_date = fields.Date()
    end_date = fields.Date()
    objective = fields.Text()

    # many2one field
    # Una fase de una mision puede destar asociada a una misión
    mission_id = fields.Many2one(comodel_name='space_mission.mission', string='Mission')
    
    
class Astronaut(models.Model):
    _name = 'space_mission.astronaut'

    name = fields.Char()
    nationality = fields.Char()
    skills = fields.Text()
    photo = fields.Binary(attachment=True)

    # many2one field
    spacecraft_id = fields.Many2one(comodel_name='space_mission.spacecraft', string='Spacecraft')

    # many2many field
    # Un astronauta puede estar asociado a una o varias misiones, y una mision puede tener uno o varios astronautas
    missions = fields.Many2many(comodel_name='space_mission.mission', 
                                relation='mission_astronaut_rel', column1='astronaut_id', 
                                column2='mission_id', string='Missions')
    