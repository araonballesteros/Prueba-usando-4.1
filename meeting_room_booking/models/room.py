# -*- coding: utf-8 -*-
from odoo import models, fields


class MeetingRoom(models.Model):
    """Modelo para definir las salas de reuniones"""
    _name = 'meeting.room'
    _description = 'Sala de reuniones'

    # Campos basicos de la sala
    name = fields.Char(string='Nombre', required=True)
    capacity = fields.Integer(string='Capacidad', required=True)
    location = fields.Char(string='Ubicacion')
    availability = fields.Boolean(string='Disponible', default=True)
