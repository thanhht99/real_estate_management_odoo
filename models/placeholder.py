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

    placeholder_line = fields.One2many('rem.placeholder.line', 'placeholder_id', string="Placeholder Lines", copy=True, auto_join=True)


    # products_list = fields.Selection('products', string="List of products", required=True)

    # @api.onchange('cart_id')
    # def onchange_cart(self):
    #     products = self.cart_id.line_ids.mapped(lambda line: line.product_id)
    #     return {
    #         'domain': {
    #             'product_id': [('id', 'in', products.ids)]
    #         }
    #     }
    
class PlaceholderLine(models.Model):
    _name = 'rem.placeholder.line'

    _logger = logging.getLogger(__name__)

    placeholder_id = fields.Many2one('rem.placeholder')
    cart_name = fields.Char(string='Cart Name')
    product_id = fields.Many2one('product.product', string='Product', change_default=True, ondelete='restrict')

    @api.onchange('placeholder_id')
    def a_id_onchange(self):
        if self.placeholder_id:
            self.cart_name = self.placeholder_id.cart.name