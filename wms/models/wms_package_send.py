from odoo import _, fields, models, api


class PackageSend(models.Model):
    _name = 'wms.package.send'
    _description = 'Send package'

    name = fields.Char(string='Send # ', required=True, index=True, default=lambda self: _('New'))

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
        comodel_name='wms.package.send.line',
        inverse_name='doc_id',
    )

    status_id = fields.Many2one(
        comodel_name='wms.package.status',
        default=lambda self: self.env.ref('wms.pSent').id,
        store=False,
    )
    note = fields.Html()

    @api.depends('package_move_ids')
    def _compute_package_qty(self):
        for rec in self:
            rec.package_qty = len(rec.package_move_ids)

    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('wms.send.sequence') or _('New')
        return super(PackageSend, self).create(vals)

    def write(self, vals):
        res = super(PackageSend, self).write(vals)
        for rec in self:
            for line in rec.package_move_ids:
                line.package_id.write({'status_id': self.status_id.id})

class Package_Send_line(models.Model):
    _name = 'wms.package.send.line'
    _description = 'Package send lines'

    package_id = fields.Many2one(
        comodel_name='wms.package',
        string='Package',
        required=True,
        domain=lambda self: [('status_id', '=', self.env.ref('wms.pArrived').id), ]
    )

    doc_id = fields.Many2one(
        comodel_name='wms.package.send'
    )
