# -*- coding: utf-8 - LUIS FELIPE PATERNINA VITAL -*-

 from odoo import models, fields, api


class entretamiento(models.Model):
     _name = 'entretamiento.entretamiento'
     _description = 'clase de entretamiento'

     name = fields.Char()
     apellido = fields.Char()
     telefono = fields.Char()
     value = fields.Integer()
     value2 = fields.Float(compute="_value_pc", store=True)
     description = fields.Text()

     @api.depends('value')
     def _value_pc(self):
         for record in self:
             record.value2 = float(record.value) / 100

            