import logging
from odoo import fields, models

_logger = logging.getLogger(__name__)


class ChangePackageStatusMulti(models.TransientModel):
    """Allow to change package status
    to selected packages or to one package
    """
    _name = 'wms.change.package.status.multi.wizard'
    _description = 'Wizard for change package status'

    new_package_status = fields.Many2one(
        comodel_name='wms.package.status',
        string="New status")

    def action_set_new_status(self):
        # set new status to every selected package
        active_ids = self.env.context.get('active_ids')
        package_ids = self.env['wms.package'].browse(active_ids)
        for package in package_ids:
            package.status_id = self.new_package_status.id
