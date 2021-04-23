# # -*- coding: utf-8 -*-
# from odoo import api, fields, models, tools, _
# from odoo.exceptions import UserError, ValidationError


# class create(models.Model):
#     _name = "cart"
#     # _inherit = ''
#     _description = "My cart model"

#     cart_name = fields.Char('Cart Name', required=True)
#     # gender = fields.Selection([
#     #     ('male', 'Male'),
#     #     ('female', 'Female')
#     # ], string='Gender', default='male')
#     description = fields.Text('Cart Description')
#     status = fields.Boolean('Status Cart')
#     cart_image = fields.Binary(
#         "Cart Image", attachment=True, help="Cart Image")
#     product_ids = fields.Many2many(comodel_name='product.product',
#                                    string="Related Products",
#                                    relation='property_product_rel',
#                                    column1='col_property_id',
#                                    column2='col_product_id')

#     property_code = fields.Many2many('property', string="Sản phẩm")
