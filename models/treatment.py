# -*- coding: utf-8 -*-

from odoo import fields, models, api,_
from odoo.exceptions import UserError

class treatment(models.Model):
    _name= 'treatment'
    _description = 'Tratamientos'

    cod_treatment = fields.Char(string = 'Código de tratamient', required=True, help='Ingrese codigo de tratamiento')
    name = fields.Char(string= 'Nombre de tratamiento', required=True, help='Ingrese nombre de tratamiento')
    doctor_treatment = fields.Char(string= 'Medico tratante', required=True, help='Ingrese nombre de medico tratante')

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100): # Permite buscar ya se por codigo o por nombre
        args = args or []
        domain = ['|', ('cod_treatment', operator, name), ('name', operator, name)] 
        records = self.search(domain + args, limit=limit)
        return records.name_get()

    def name_get(self): # Combina el código y el nombre
        result = []
        for record in self:
            name = f"{record.cod_treatment} - {record.name}"  
            result.append((record.id, name))
        return result

    @api.constrains('cod_treatment')
    def _verify_cod_treatment(self):
        for rec in self:
            if rec.cod_treatment and '026' in rec.cod_treatment:
                raise UserError(_("La secuencia no puede ser 026 intente con otra combinacion"))