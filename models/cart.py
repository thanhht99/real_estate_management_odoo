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

class Cart(models.Model):
    _name = 'rem.cart'
    _description = "Cart Real Estate"

    name = fields.Char(string="Cart name", required=True)
    # state = fields.Selection()
    date_of_sale = fields.Datetime(string='Date of sale', required=True)
    end_date = fields.Datetime(string='End date', required=True)

    project = fields.Many2one('rem.project', string="Project", required=True)

    # products_list =  fields.Many2many('product.product', string="Product", required=True)


    cart_line = fields.One2many('rem.cart.line', 'cart_id', string="Cart Lines", copy=True, auto_join=True)

    # @api.onchange('project')
    # def onchange_project(self):
    #     self.cart_line['domain'] = {'product_id': [('project_id', '=', self.project)]}
    #     return self.cart_line


    # def create(self,values)


class CartLine(models.Model):
    _name = 'rem.cart.line'

    cart_id = fields.Many2one('rem.cart')
    project_code = fields.Char(string='Code Project')
    product_id = fields.Many2one('product.product', string='Product', change_default=True, ondelete='restrict')

    price = fields.Char(string="Price")

    @api.onchange('cart_id')
    def a_id_onchange(self):
        if self.cart_id:
            self.project_code = self.cart_id.project.code