import logging
from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class PackageArriveVizard(models.TransientModel):
    """When the package arrives to warehouse,
        worker need to find it db, write the weight
        Wizard will write the next status "Arrived"
    """
    _name = 'wms.package.arrive.wizard'
    _description = 'Wizard for save arrives'

    track_number = fields.Char()
    package_id = fields.Many2one(comodel_name='wms.package')
    weight = fields.Float(digits=(8, 3))

    @api.onchange('track_number')
    def _onchange_track_number(self):
        # find the package by track number
        package = self.env['wms.package'].search([('track_number', '=', self.track_number)], limit=1)
        if package:
            self.package_id = package.id
        else:
            self.package_id = False

    def action_set_arrive(self):
        # Write: weight, new status, may somth. else
        self.package_id.weight = 2
