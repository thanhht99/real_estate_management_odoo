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

    open_sale_location = fields.Char(string="Open sale location", required=True)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('open', 'Sale Open'),
        ('soldout', 'Sold Out'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', track_sequence=3, default='draft')
    # products_list =  fields.Many2many('product.product', string="Product", required=True)

    cart_line = fields.One2many('rem.cart.line', 'cart_id', string="Cart Lines", copy=True, auto_join=True)

    placeholder_count = fields.Integer(
        '# Placeholders', 
        compute='_compute_placeholder_count',
        help="The number of placeholder")
    
    # def create(self,values)
    @api.multi
    def action_open(self):
        self.ensure_one()        
        products = self.cart_line.mapped('product_id')
        if products.filtered(lambda p: p.sale_opening == 'opening'):
            raise UserError("Products already in the first open other sell")
        products.write({'sale_opening': 'opening'})
        self.state = 'soldout'

    @api.multi
    def action_soldout(self):
        self.ensure_one()
        self.state = 'done'

    @api.multi
    def action_open_placeholder(self):
        return {
            'name': _('Placeholders'),
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'rem.placeholder',
            'view_id': False,
            'type': 'ir.actions.act_window',
            'domain': [('cart', '=', self.id)],
            'context': {
                'default_cart': self.id,
            }
        }
        
    def _compute_placeholder_count(self):
        data_obj = self.env['rem.placeholder'].search([('cart', '=', self.id)])
        _logger.exception('--------------------------------------------------------  %s', data_obj)
        self.placeholder_count = len(data_obj)

    # def _compute_placeholder_count(self):
    #     read_group_res = self.env['rem.placeholder'].read_group([('cart', 'child_of', self.ids)], ['cart'], ['cart'])
    #     group_data = dict((data['cart'][0], data['cart_count']) for data in read_group_res)
    #     for cart1 in self:
    #         placeholder_count = 0
    #         for sub_cart1_id in cart1.search([('id', 'child_of', cart1.id)]).ids:
    #             placeholder_count += group_data.get(sub_cart1_id, 0)
    #         cart1.placeholder_count = placeholder_count

class CartLine(models.Model):
    _name = 'rem.cart.line'

    _logger = logging.getLogger(__name__)

    cart_id = fields.Many2one('rem.cart')
    project_code = fields.Char(string='Code Project')
    product_id = fields.Many2one('product.product', string='Product', change_default=True, ondelete='restrict')

    price = fields.Float(string="Price")

    @api.onchange('cart_id')
    def a_id_onchange(self):
        output = "sample result"
        _logger.exception('--------------------------------------------------------  %s', output)
        if self.cart_id:
            self.project_code = self.cart_id.project.code


