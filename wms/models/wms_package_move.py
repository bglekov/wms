# from odoo import fields, models
#
#
# class PackageMove(models.Model):
#     _name = 'wms.package.move'
#     _description = 'Package move'
#
#     package_id = fields.Many2one(
#         comodel_name='wms.package',
#         string='Package',
#         required=True,
#     )
#
#     status_id = fields.Many2one(
#         comodel_name='wms.package.status',
#         string='Status',
#         required=True,
#     )
#
#     doc_id = fields.Many2one(
#         comodel_name='wms.package.arrive'
#     )
