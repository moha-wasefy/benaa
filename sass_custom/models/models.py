# -*- coding: utf-8 -*-

from odoo import models,fields, api, _
from odoo.exceptions import ValidationError


class sass_custom(models.Model):
    _inherit = 'product.template'

    invoice_nums = fields.Integer(
        string='Invoice Nums',
        readonly=True)

    inventory_nums = fields.Integer(
        string='Inventory Nums',
        readonly=True)

    employee_nums = fields.Integer(
        string='Employee Nums',
        readonly=True)

    pos_nums = fields.Integer(
        string='Pos Nums',
        readonly=True)

    @api.model
    def create(self, vals):
        res = super(sass_custom, self).create(vals)
        for rec in res:
            if rec.name == 'باقة بداية':
                rec.invoice_nums =30
                rec.inventory_nums =20
                rec.employee_nums =18
                rec.pos_nums =10
            elif rec.name == 'باقة متوسطة':
                rec.invoice_nums = 40
                rec.inventory_nums = 30
                rec.employee_nums = 20
                rec.pos_nums = 15
            elif rec.name == 'باقة متقدمة':
                rec.invoice_nums = 50
                rec.inventory_nums = 40
                rec.employee_nums = 30
                rec.pos_nums = 20

        return res

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    @api.model
    def create(self, vals):
        package = self.env.company.sass_package
        if package:
            current_count = self.env['hr.employee'].search_count([('company_id', '=', self.env.company.id)])
            if current_count > package.employee_nums:
                raise ValidationError(_('تم الوصول للحد الأقصى لعدد الموظفين في هذه الباقة.'))
        return super().create(vals)

class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.model
    def create(self, vals):
        package = self.env.company.sass_package
        if package and vals.get('move_type') in ['out_invoice', 'in_invoice']:
            current_count = self.env['account.move'].search_count([
                ('company_id', '=', self.env.company.id),
                ('move_type', '=', vals['move_type'])
            ])
            if current_count > package.invoice_nums:
                raise ValidationError(_('تم الوصول للحد الأقصى لعدد الفواتير في هذه الباقة.'))
        return super().create(vals)

class PosConfig(models.Model):
    _inherit = 'pos.config'

    @api.model
    def create(self, vals):
        package = self.env.company.sass_package
        if package:
            current_count = self.env['pos.config'].search_count([
                ('company_id', '=', self.env.company.id)
            ])
            print(current_count)
            if current_count > package.pos_nums:
                raise ValidationError(_('تم الوصول للحد الأقصى لعدد نقاط البيع في هذه الباقة.'))
        return super().create(vals)

class StockWarehouse(models.Model):
    _inherit = 'stock.warehouse'

    @api.model
    def create(self, vals):
        package = self.env.company.sass_package
        if package:
            current_count = self.env['stock.warehouse'].search_count([
                ('company_id', '=', self.env.company.id)
            ])
            if current_count > package.inventory_nums:
                raise ValidationError(_('تم الوصول للحد الأقصى لعدد المخازن في هذه الباقة.'))
        return super().create(vals)

