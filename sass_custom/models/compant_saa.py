from odoo import fields, models, api

class ResCompany(models.Model):
    _inherit = 'res.company'

    sass_package = fields.Many2one(
        'product.template',
        string="Active SaaS Package",
        compute='_compute_sass_package',
        readonly=True
    )

    @api.depends('name')  # أي حقل يخلّي Odoo يعيد الحساب لو حبيت
    def _compute_sass_package(self):
        for company in self:
            package = self.env['product.template'].search([
                ('name', 'in', ['باقة بداية', 'باقة متوسطة', 'باقة متقدمة'])
            ], limit=1)

            company.sass_package = package
