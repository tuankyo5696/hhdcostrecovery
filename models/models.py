# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class hhd_cost_recovery(models.Model):
#     _name = 'hhd_cost_recovery.hhd_cost_recovery'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100