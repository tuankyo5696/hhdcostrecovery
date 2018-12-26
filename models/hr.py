# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import base64
import logging

from odoo import api, fields, models



class EmployeeCategory(models.Model):

    _name = "hr.employee.category"
    _description = "Employee Category"

    name = fields.Char(string="Employee Tag", required=True)
    color = fields.Integer(string='Color Index')
    employee_ids = fields.Many2many('hr.employee', 'employee_category_rel', 'category_id', 'emp_id', string='Employees')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag name already exists !"),
    ]



class Employee(models.Model):
    _name = "hr.employee"
    _description = "Employee"
    _order = 'name'

    name = fields.Char(related='resource_id.name', store=True, oldname='name_related', readonly=False)
    user_id = fields.Many2one('res.users', 'User', related='resource_id.user_id', store=True, readonly=False)
    active = fields.Boolean('Active', related='resource_id.active', default=True, store=True, readonly=False)  
    country_id = fields.Many2one(
        'res.country', 'Nationality (Country)', groups="hr.group_hr_user")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], groups="hr.group_hr_user", default="male")
    
    birthday = fields.Date('Date of Birth', groups="hr.group_hr_user")
    
        domain="[('partner_id', '=', address_home_id)]",
        groups="hr.group_hr_user",
        help='Employee bank salary account')

    manager_id = fields.Many2one('hr.employee', 'Manager')
   
    @api.onchange('manager_id')
    def _onchange_employee(self):
        self.manager_id =self.Manager

class HhdCostRecovery(models.Model):
    _name= "hhd.cost.recovery"
    _description= " HHD Cost Recovery"

    customer_name = fields.Char(related='resource_id.name', store=True, oldname='name_related', readonly=False)
    gender_cs = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], groups="hr.group_hr_user", default="male")
    
    food_cost = fields.Float()
    drink_cost= fields.Float()

    cost_recovery= fields.Float()


class HhdCostRecoveryCate(models.Model):

    _name = "hhd.cost.recovery.cate"
    _description = "Hhd Cost Recovery Category"

    name = fields.Char(string="Cost Recovery Tag", required=True)
    color = fields.Integer(string='Color Index')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag name already exists !"),
    ]
    