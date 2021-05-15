# -*- coding: utf-8 -*-
import json
import logging
from datetime import timedelta, time

from odoo import api, fields, models, _
from odoo.addons.base.models.res_partner import WARNING_MESSAGE, WARNING_HELP
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_round

_logger = logging.getLogger(__name__)

class Placeholder(models.Model):
    _name = 'rem.placeholder'
    _description = "Placeholder Real Estate"

    name = fields.Char(string="Placeholder name", required=True)

    cart = fields.Many2one('rem.cart', string="Cart", required=True)

    product_id = fields.Many2one('product.product', required=True)

    # products_list = fields.Selection('products', string="List of products", required=True)

    @api.onchange('cart_id')
    def onchange_cart(self):
        products = self.cart_id.line_ids.mapped(lambda line: line.product_id)
        return {
            'domain': {
                'product_id': [('id', 'in', products.ids)]
            }
        }
    
