from odoo import fields, models, api


class Address_Mixin(models.Model):
    # _name = 'wms.country'
    _description = 'Countries'
    _inherit = 'res.country'

    # name = fields.Char()
    search_deep = fields.Integer()