from odoo import fields, models, api


class Packages(models.Model):
    _name = 'wms.package'
    _description = 'Packages'

    track_number = fields.Char(required=True)
    warehouse_id = fields.Many2one(
        comodel_name="res.company",
        required=True,
        index=True,
    )
    status_id = fields.Many2one(
        comodel_name="wms.package.status",
        required = True,
        index = True,
        default=lambda self: self.env.ref('wms.pDeclared').id
    )

