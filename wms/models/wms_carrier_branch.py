from odoo import fields, models


class CarrierBranches(models.Model):
    _name = 'wms.carrier.branch'
    _description = 'Carrier Branches'

    name = fields.Char()
    code = fields.Char(required=True)
    status = fields.Selection(
        selection=[
            ('open', 'Open'),
            ('closed', 'Closed'),
        ]
    )

    carrier_id = fields.Many2one(
        comodel_name='wms.carrier',
        string='Carrier',
        required=True,
        index=True,
    )
