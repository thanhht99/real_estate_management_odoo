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

    contact = fields.Many2many('res.partner', string="Contact", required=True)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('open', 'Sale Open'),
        ('soldout', 'Sold Out'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', track_sequence=3, default='draft')
    # products_list =  fields.Many2many('product.product', string="Product", required=True)

    cart_line = fields.One2many('rem.cart.line', 'cart_id', string="Cart Lines", copy=True, auto_join=True)
    
    # def create(self,values)
    @api.multi
    def action_open(self):
        self.ensure_one()
        self.state = 'open'
        self.cart_line.mapped('product_id').write({'sale_opening': 'opening'})

    @api.multi
    def action_soldout(self):
        self.ensure_one()
        self.state = 'soldout'

class CartLine(models.Model):
    _name = 'rem.cart.line'

    _logger = logging.getLogger(__name__)

    cart_id = fields.Many2one('rem.cart')
    project_code = fields.Char(string='Code Project')
    product_id = fields.Many2one('product.product', string='Product', change_default=True, ondelete='restrict')

    price = fields.Float(string="Price", compute="_compute_price")

    @api.depends('product_id', 'cart_id.project')
    def _compute_price(self):
        for rec in self:
            line = rec.filtered(lambda line: line.product_id == rec.product_id)
            rec.list_price = line.price

    @api.onchange('cart_id')
    def a_id_onchange(self):
        output = "sample result"
        _logger.exception('--------------------------------------------------------  %s', output)
        if self.cart_id:
            self.project_code = self.cart_id.project.code


