# -*- coding: utf-8 -*-
import json
import logging
from datetime import timedelta, time

from odoo import api, fields, models, _
from odoo.addons.base.models.res_partner import WARNING_MESSAGE, WARNING_HELP
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_round

_logger = logging.getLogger(__name__)

class Cart(models.Model):
    
    _inherit = "account.invoice"

    agency_list = fields.Many2many('rem.agency', string='Agency List')