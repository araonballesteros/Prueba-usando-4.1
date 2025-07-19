# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class MeetingBooking(models.Model):
    """Modelo para las reservas de salas"""
    _name = 'meeting.booking'
    _description = 'Reserva de sala'

    # Datos de la reserva
    name = fields.Char(string='Referencia', default='New', copy=False)
    room_id = fields.Many2one('meeting.room', string='Sala', required=True)
    start_time = fields.Datetime(string='Inicio', required=True)
    end_time = fields.Datetime(string='Fin', required=True)
    booked_by = fields.Many2one(
        'res.users', string='Reservado por', default=lambda self: self.env.user
    )

    @api.constrains('room_id', 'start_time', 'end_time')
    def _check_overlap(self):
        """Valida que no existan reservas en el mismo horario"""
        for rec in self:
            if not rec.room_id or not rec.start_time or not rec.end_time:
                continue
            domain = [
                ('id', '!=', rec.id),
                ('room_id', '=', rec.room_id.id),
                ('start_time', '<', rec.end_time),
                ('end_time', '>', rec.start_time),
            ]
            if self.search_count(domain):
                raise ValidationError(
                    'La sala ya esta reservada en ese horario.'
                )
