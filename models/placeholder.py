# -*- coding: utf-8 -*-
import json
import logging
from datetime import timedelta, time

from odoo import api, fields, models, _
from odoo.addons.base.models.res_partner import WARNING_MESSAGE, WARNING_HELP
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_round

from odoo.addons import decimal_precision as dp

_logger = logging.getLogger(__name__)


class Placeholder(models.Model):
    _name = 'rem.placeholder'
    
    _description = "Placeholder Real Estate"

    name = fields.Char(string="Placeholder name", required=True)

    cart = fields.Many2one('rem.cart', string="Cart", required=True)

    # product = fields.Many2one('product.product', required=True)

    placeholder_line = fields.One2many(
        'rem.placeholder.line', 'placeholder_id', string="Placeholder Lines", copy=True, auto_join=True)
    # products_list = fields.Selection('products', string="List of products", required=True)


class PlaceholderLine(models.Model):
    _name = 'rem.placeholder.line'

    placeholder_id = fields.Many2one('rem.placeholder')

    product_id = fields.Many2one(
        'product.product', string='Product', change_default=True, ondelete='restrict')

    price = fields.Float(string="Unit Price", compute="_compute_price")

    @api.depends('product_id', 'placeholder_id.cart')
    def _compute_price(self):
        for rec in self:
            line = rec.placeholder_id.cart.cart_line.filtered(lambda line: line.product_id == rec.product_id)
            rec.price = line.price

    @api.onchange('placeholder_id')
    def onchange_cart(self):
        output = "sample result"
        _logger.exception('--------------------------------------------------------  %s', output)         
        products = self.placeholder_id.cart.cart_line.mapped(lambda line: line.product_id)
        return {
            'domain': {
                'product_id': [('id', 'in', products.ids)]
            }            
        }

        

