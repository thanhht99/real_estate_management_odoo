import logging
from datetime import timedelta
from odoo import models, fields, api, exceptions, _

_logger = logging.getLogger(__name__)

class Project(models.Model):
    _name = 'rem.project'
    _description = "Project Real Estate"

    code = fields.Char(string="Project code", required=True)
    name = fields.Char(string="Project name", required=True)
    investor = fields.Char(string="Investor", required=True)
    location = fields.Text(string="Project location", required=True)
    scale = fields.Text(string="Project scale")
    area = fields.Char(string="Project area", required=True)
    legal = fields.Text(string="Project legal")
    status = fields.Char(string="Project status")
    type = fields.Char(string="Project type", required=True)
    construction_form = fields.Char(string="Construction form")
    time_book_receipt = fields.Date(string="Time of land allocation/book receipt")


    price = fields.Char(string="Project selling price", required=True)
    bank_support = fields.Char(string="Bank support")
    discount = fields.Float(string="Discount",)

    payment_methods = fields.Char(string="Payment methods")

    product_count = fields.Integer(
        '# Products', 
        compute='_compute_product_count',
        help="The number of Products")

    @api.multi
    def action_open_product(self):
        return {
            'name': _('Products'),
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'product.product',
            'view_id': False,
            'type': 'ir.actions.act_window',
            'domain': [('project_id', '=', self.id)],
            'context': {
                'default_project_id': self.id,
            }
        }

    def _compute_product_count(self):
        data_obj = self.env['product.product'].search([('project_id', '=', self.id)])
        _logger.exception('--------------------------------------------------------  %s', data_obj)
        self.product_count = len(data_obj)


    _sql_constraints = [        
        ('code_unique',
         'UNIQUE(code)',
         "The code must be unique"),
    ]

