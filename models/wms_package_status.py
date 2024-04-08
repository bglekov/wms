from odoo import fields, models, api


class PackageStatus(models.Model):
    _name = 'wms.package.status'
    _description = 'Package statuses'

    name = fields.Char()
