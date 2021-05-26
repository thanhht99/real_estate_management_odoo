from datetime import timedelta
from odoo import models, fields, api, exceptions, _


class PropertyGroup(models.Model):
    _name = 'rem.property.group'
    _description = "Set group for property"

    name = fields.Char(string="Group name", required=True)
    isActive = fields.Boolean(default='True')


class PropertyType(models.Model):
    _name = 'rem.property.type'
    _description = "Set type for property"

    name = fields.Char(string="Type name", required=True)
    isActive = fields.Boolean(default='True')


class PropertyAddSet(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    sale_opening = fields.Selection([('opening', 'Opening'), ('noopening', 'Noopening'), (
        'sold', 'Sold'), ('deposited', 'Deposited')], 'Set', default='noopening', help='')

    group_name = fields.Many2one('rem.property.group', string='Group Name')
    group_isActive = fields.Boolean('Group', related='group_name.isActive')

    type_name = fields.Many2one('rem.property.type', string='Type Name')
    type_isActive = fields.Boolean('Type', related='type_name.isActive')
