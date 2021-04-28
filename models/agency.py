from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class Agency(models.Model):
    _name = "rem.agency"
    _description = "My agency model"

    name = fields.Char('Agency Name', required=True)
    company  = fields.Char('Agency Company', required=True)
    address  = fields.Text('Agency Address', required=True)
    tax_code  = fields.Char('Tax Code', required=True)
    phone  = fields.Char('Phone', default='Đang cập nhật')
    mobile  = fields.Char('Mobile', default='Đang cập nhật')
    email  = fields.Char('Email', default='Đang cập nhật')
    website  = fields.Char('Website', default='Đang cập nhật')

    partner_type = fields.Selection([
        ('main', 'Main'),
        ('sub', 'Sub')
    ], string='Partner type', default='sub')
    contact_info  = fields.Text('Contact Info', default='Đang cập nhật')

    _sql_constraints = [            
        ('name_unique',
         'UNIQUE(name)',
         "The course title must be unique"),
    ]