# -*- coding: utf-8 -*-
import json
import logging
from datetime import timedelta, time

from odoo import api, fields, models, _
from odoo.addons.base.models.res_partner import WARNING_MESSAGE, WARNING_HELP
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_round

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _name = "sale.order"
    _inherit = "sale.order"
    _description = "Extend sale order model"

    # agency_list = fields.Many2many('rem.agency', string='Agency List')
    sale_date = fields.Datetime(string='Sale Date', required=True)

    partner_group = fields.Selection([
        ('normal', 'Normal'),
        ('real_estate_investors', 'Real Estate Investors'),
        ('businessmen', 'Businessmen')
    ], string='Partner Group', default='normal')