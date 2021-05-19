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

    

<<<<<<< HEAD
    # @api.model
    # def create(self,values):
    #     valp = {}
    #     valp['sale_opening'] = 'opening'
    #     prd = self.env['product.product'].create(valp)
    #     values['cart_line'] = prd.id
    #     new_record = super(Cart, self).create(values)
    #     return new_record
    

=======

    # def create(self,values)
    @api.multi
    def action_open(self):
        self.ensure_one()
        self.state = 'open'
        self.cart_line.mapped('product_id').write({'sdsd': dsd})
>>>>>>> origin/origin/dibang

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
<<<<<<< HEAD
            final_str = "%s" % (product_id)
            output = "sample result"
            _logger.exception('--------------------------------------------------------  %s', final_str)
            _logger.exception('-----0000000------------------------  %s', output)


    @api.multi
    def write(self,vals):
        vals.product_id.update({'sale_opening': 'opening'})
        output = "sample result"
        _logger.exception('--------------------------------------------------------  %s', output)
        return super(CartLine, self).write(vals) 

    # @api.model
    # def create(self,vals):
    #     valp = {}
    #     # valp['id'] = vals['cart_line.product_id.product_tmpl_id']
    #     valp['list_price'] = vals['price']
    #     valp['sale_opening'] = 'opening'
    #     prd = self.env['product.template'].create(valp)
    #     vals['product_id'] = prd.id
    #     new_record = super(CartLine, self).create(vals)
    #     output = "sample result11111111111111111111111111111111"
    #     _logger.exception('------ewr322222222222222222242222222222222222222222222222---------  %s', output)
    #     return new_record
    
    
=======


>>>>>>> origin/origin/dibang
