from odoo import fields, models, api


class UserAddress(models.Model):
    _name = 'wms.user.address'
    _description = 'Senders or recipients'
    _inherit = "wms.address.mixin"

    name = fields.Char()

    first_name = fields.Char(required=True)
    last_name = fields.Char()
    phone = fields.Char()

    client_id = fields.Many2one(
        comodel_name="res.partner",
        required=True
    )

    # Add 2 cases, because it possible to be a sender and recipient at 1 time
    is_sender = fields.Boolean()
    is_recipient = fields.Boolean()

    # looks like 0-Door 1-branch, default Door
    delivery_type = fields.Integer()

    carrier_id = fields.Many2one(
        comodel_name="wms.carrier"
    )
