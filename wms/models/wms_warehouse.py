from odoo import fields, models


class Warehouse(models.Model):
    _inherit = 'res.company'

    # name = fields.Char()
    custom_address = fields.Char()
