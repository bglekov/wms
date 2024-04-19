from odoo import _, api, fields, models


class PackageArrive(models.Model):
    _name = 'wms.package.arrive'
    _description = 'Arrive'

    name = fields.Char(string='Arrive # ', required=True, index=True, default=lambda self: _('-'))

    warehouse_id = fields.Many2one(
        comodel_name='res.company',
        required=True,
        index=True,
    )

    package_qty = fields.Integer(
        string='Q-ty',
        compute='_compute_package_qty',
        store=False,
    )

    package_move_ids = fields.One2many(
        comodel_name='wms.package.arrive.line',
        inverse_name='doc_id',
    )

    status_id = fields.Many2one(
        comodel_name='wms.package.status',
        default=lambda self: self.env.ref('wms.pArrived').id,
        store=False,
    )

    @api.depends('package_move_ids')
    def _compute_package_qty(self):
        for rec in self:
            rec.package_qty = len(rec.package_move_ids)

    def create(self, vals):
        if vals.get('name', _('-')) == _('-'):
            vals['name'] = self.env['ir.sequence'].next_by_code('wms.arrive.sequence') or _('-')
        # return super(PackageArrive, self).create(vals)
        res = super().create(vals)
        for line in res.package_move_ids:
            line.package_id.write({'status_id': res.status_id.id, 'weight': line.weight})
        return res

    def write(self, vals):
        res = super(PackageArrive, self).write(vals)
        for rec in self:
            for line in rec.package_move_ids:
                line.package_id.write({'status_id': self.status_id.id, 'weight': line.weight})
        return res

class Package_Arrive_line(models.Model):
    _name = 'wms.package.arrive.line'
    _description = 'Package arrive line'

    package_id = fields.Many2one(
        comodel_name='wms.package',
        string='Package',
        required=True,
        domain=lambda self: [('status_id', '=', self.env.ref('wms.pDeclared').id), ]
    )

    weight = fields.Float(digits=(8, 3))

    doc_id = fields.Many2one(
        comodel_name='wms.package.arrive'
    )
