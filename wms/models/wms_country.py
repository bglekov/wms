from odoo import fields, models


class Country(models.Model):
    # _name = 'wms.country'
    _description = 'Countries'
    _inherit = 'res.country'

    # name = fields.Char()
    search_deep = fields.Integer()
