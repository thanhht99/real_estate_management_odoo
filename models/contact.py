from ast import literal_eval
from operator import itemgetter
import time

from odoo import api, fields, models, _
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.exceptions import ValidationError
from odoo.addons.base.models.res_partner import WARNING_MESSAGE, WARNING_HELP

class Percentage(models.Model):
    _name = 'rem.percentage'
    _description = "Percentage for property"

    name = fields.Char(string="Percentage name", required=True)
    percentage = fields.Float(string="Percentage")

class PercentageOfContact(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'    

    pct = fields.Many2one('rem.percentage',string='Percentage Name')

    property_count = fields.Integer(
        '# Properties', 
        # compute='_compute_property_count',
        help="The number of Properties")