from odoo import fields, models


class AddressMixin(models.AbstractModel):
    _name = 'wms.address.mixin'
    _description = 'Countries'

    country_id = fields.Many2one(
        comodel_name="res.country",
        required=True,
    )

    state_id = fields.Many2one(
        comodel_name="res.country.state",
        domain="[('country_id', '=', country_id)]",
    )

    city = fields.Char()
    street = fields.Char()
    house = fields.Char(size=5)
    flat = fields.Integer()

    zip = fields.Char(size=7)
