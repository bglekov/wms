from odoo import fields, models, api


class Carriers(models.Model):
    _name = 'wms.carrier'
    _description = 'First/Last miles Carriers'

    name = fields.Char()
    is_active = fields.Boolean(default=True, store=True)

