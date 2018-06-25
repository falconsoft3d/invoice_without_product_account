# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
import os, datetime
from openerp.tools.translate import _
from openerp.exceptions import Warning

class ResPartner(models.Model):

    _inherit = 'res.partner'

    account_in_without_product_id = fields.Many2one(
        'account.account', 
        string='Cuenta de ingresos', 
        help="Cuenta contable auxiliar de ingresos para facturas que se crean sin productos. Solo con una descripción.")
        
    account_out_without_product_id = fields.Many2one(
        'account.account', 
        string='Cuenta de gastos', 
        help="Cuenta contable auxiliar de gastos para facturas que se crean sin productos. Solo con una descripción.")
