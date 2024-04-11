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
        required=True,
        index=True,
    )

    # Add 2 cases, because it possible to be a sender and recipient at 1 time
    is_sender = fields.Boolean(index=True)
    is_recipient = fields.Boolean(index=True)

    # looks like 0-Door 1-branch, default Door
    delivery_type = fields.Integer()

    carrier_id = fields.Many2one(
        comodel_name="wms.carrier"
    )

    @api.onchange('first_name', 'last_name')
    def _compute_name(self):
        # self.ensure_one()
        for rec in self:
            if rec.first_name and rec.last_name:
                rec.name = "%s %s" % (rec.first_name, rec.last_name)
            elif rec.first_name:
                rec.name = rec.first_name
            elif rec.last_name:
                rec.name = rec.last_name
            # rec.name = rec.first_name + ' ' + rec.last_name
