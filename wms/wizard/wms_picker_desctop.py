from odoo import fields, models, api


class PickerDesctop(models.TransientModel):
    _name = 'wms.picker.desctop'
    _description = 'Picker Desctop'

    search_track_number = fields.Char()
    search_package_id = fields.Many2one(comodel_name='wms.package')

    @api.onchange('search_track_number')
    def _onchange_search_track_number(self):
        # find the package by track number
        package = self.env['wms.package'].search(
            [('name', '=', self.search_track_number)], limit=1)
        if package:
            self.search_package_id = package.id
        else:
            self.search_package_id = False
