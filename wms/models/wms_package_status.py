from odoo import fields, models


class PackageStatus(models.Model):
    _name = 'wms.package.status'
    _description = 'Package statuses'
    _order = 'order'

    name = fields.Char()
    order = fields.Integer()
