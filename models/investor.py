from datetime import timedelta
from odoo import models, fields, api, exceptions, _

class Investor(models.Model):
    _name = 'rem.investor'
    _description = "Investor's Information "

    name = fields.Char(string="Investor's Name", required=True)

    image = fields.Binary("Image", attachment=True,)
    image_medium = fields.Binary("Medium-sized image", attachment=True)
    image_small = fields.Binary("Small-sized image", attachment=True)

    vendor = fields.Char(string="Vendor Name", required=True)

    isVendor = fields.Boolean(tring="Is Vendor", default=True)
    isCustomer = fields.Boolean(string="Is Customer", default=True)
    active = fields.Boolean(default=True)

    address = fields.Char(string="Address")
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    website = fields.Char(string="Website Home Page")
    description = fields.Char(string="Ab Company")
    taxcode = fields.Char(string="Tax Code")
    mobile = fields.Char(string="Mobile")

    bank_ids = fields.One2many('rem.vendorbank', 'vendor_id', string="Bank")
    acc_number = fields.Char('Account Number', required=True)


class Bank(models.Model):
    _name = 'rem.bank'
    _description = "Bank"

    name = fields.Char(string="Bank", rrquired=True)
    bank_code = fields.Char(string="Bank Code", rrquired=True)
    bank_branch = fields.Char(string="Bank Branch", rrquired=True)
    

class VendorBank(models.Model):
    _name = 'rem.vendorbank'
    _description = "Account of Vendor with Banking"

    vendor_id = fields.Many2one('rem.investor', string="Vendor Bank")
    bank_id = fields.Many2one('rem.bank', string='Bank')
    bank_name = fields.Char(related='bank_id.name', readonly=False)
    bank_code = fields.Char(related='bank_id.bank_code', readonly=False)