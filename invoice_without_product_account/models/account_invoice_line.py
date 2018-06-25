# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.tools import float_is_zero, float_compare

class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    @api.onchange('name')
    def _onchange_account_line(self):
        
        partner = self.invoice_id.partner_id
        company = self.invoice_id.company_id
        fiscal_position = self.invoice_id.fiscal_position_id
        type = self.invoice_id.type
        
        product = self.env['product.product'].search([('active','=',True)],limit=1)
        account = type == 'in_invoice' and partner.account_out_without_product_id or \
                  type == 'out_invoice' and partner.account_in_without_product_id or \
                  self.get_invoice_line_account(type, product, fiscal_position, company)
        if not self.product_id and account:
            self.account_id = account.id
