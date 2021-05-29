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

    price_holder = fields.Float(string='Cost to holder')

    partner_id = fields.Many2one('res.partner', string="Customer" ,required=True)

    payment_term = fields.Selection([
        ('nocost', 'No Cost'),
        ('oneweek', '1 Week'),
        ('twoweek', '2 Week'),
        ('onemonth', '1 Month'),
        ('twomonth', '2 Month'),
        ('sixmonth', '6 Month'),
    ])

    state = fields.Selection([
        ('draft', 'Nháp'),
        ('validate', 'Đã thanh toán'),
        ('paid', 'Done'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
    ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', track_sequence=3, default='draft')

    payment_type = fields.Selection([
        ('bank', 'Bank(VND)'),
        ('cash', 'Cash(VND)')
    ])
    placeholder_date = fields.Date(string='Ngày đặt chổ')
    # product = fields.Many2one('product.product', required=True)
    payment_id = fields.Many2one('account.payment', string='Payment Name')

    placeholder_line = fields.One2many(
        'rem.placeholder.line', 'placeholder_id', string="Placeholder Lines", copy=True, auto_join=True)
    # products_list = fields.Selection('products', string="List of products", required=True)

    @api.multi
    def action_validate(self):
        self.ensure_one()
        self.state = 'validate'
        payment = self.env['account.payment'].create({
            "name": self.cart.name + '/ ' + str(self.placeholder_line.product_id.name) + '/ ' + str(self.partner_id.name),
            "payment_type": 'inbound',
            "partner_id": self.partner_id.id,
            "payment_method_id": 1,
            "partner_type": 'customer',
            "amount": self.price_holder,
            "journal_id": 7,
        })
        self.payment_id = payment

    @api.multi
    def action_paid(self):
        self.ensure_one()
        self.state = 'paid'
        self.placeholder_line.mapped('product_id').write(
            {'sale_opening': 'deposited'})

    # @api.multi
    # def action_validate_payment(self):
    #     self.ensure_one()


class PlaceholderLine(models.Model):
    _name = 'rem.placeholder.line'

    placeholder_id = fields.Many2one('rem.placeholder')

    product_id = fields.Many2one(
        'product.product', string='Product', change_default=True, ondelete='restrict')

    price = fields.Float(string="Unit Price", compute="_compute_price")

    @api.depends('product_id', 'placeholder_id.cart')
    def _compute_price(self):
        for rec in self:
            line = rec.placeholder_id.cart.cart_line.filtered(
                lambda line: line.product_id == rec.product_id)
            rec.price = line.price

    @api.onchange('placeholder_id')
    def onchange_cart(self):
        output = "sample result"
        _logger.exception(
            '--------------------------------------------------------  %s', output)
        products = self.placeholder_id.cart.cart_line.mapped(
            lambda line: line.product_id)
        return {
            'domain': {
                'product_id': [('id', 'in', products.ids),
                               ('sale_opening', '=', 'opening')]
            }
        }
