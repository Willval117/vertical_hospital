# -*- coding: utf-8 -*-

from odoo import fields, models, api, _

class Patient(models.Model):
    _name= 'patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']  
    _description = 'Pacientes'
    _rec_name = 'name'

    name = fields.Char(string='Referencia', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    complete_name = fields.Char(string='Nombre y apellido', required=True, help='Ingrese el nombre del paciente')
    dni = fields.Integer(string='DNI', required=True, help='Ingrese identificacion de paciente DNI', tracking=1)
    treatment_id = fields.Many2one('treatment',string='Tratamientos', help='Seleccione tratamiento')
    state=fields.Selection([('draft', 'Borrador'),
                            ('confirm', 'Alta'),
                            ('cancel', 'Baja')], string='Estado', default='draft', tracking=1)
    date_confirm=fields.Datetime(string='Fecha y hora de alta', compute='_date_confirm')

    @api.model
    def create(self,vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('patient') or _('New')
        res = super(Patient, self).create(vals)
        return res

    @api.depends('state')
    def _date_confirm(self):
        for rec in self:
            if rec.state == 'confirm' and not rec.date_confirm:
               rec.date_confirm = fields.Datetime.now()
            elif rec.state != 'confirm':
                rec.date_confirm = False