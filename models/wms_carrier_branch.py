from odoo import fields, models, api


class CarrierBranches(models.Model):
    _name = 'wms.carrier.branches'
    _description = 'Carrier Branches'

    name = fields.Char()
    inner_id = fields.Char()

    carrier_id = fields.Many2one(
        comodel_name='wms.carrier',
        string='Carrier',
    )