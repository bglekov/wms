from odoo import fields, models, api


class Packages(models.Model):
    _name = 'wms.package'
    _description = 'Packages'

    name = fields.Char(string="Track number", required=True)
    warehouse_id = fields.Many2one(
        comodel_name="res.company",
        required=True,
        index=True,
    )
    status_id = fields.Many2one(
        comodel_name="wms.package.status",
        required=True,
        index=True,
        default=lambda self: self.env.ref('wms.pDeclared').id
    )

    weight = fields.Float(digits=(8, 3))
    client_id = fields.Many2one(
        comodel_name="res.partner",
        required=True,
        index=True,
    )

    # sender address fields
    sender_id = fields.Many2one(
        string="Sender",
        comodel_name='wms.user.address',
        domain="[('is_sender', '=', True),('client_id', '=', client_id),]",
    )

    s_country_id = fields.Many2one(
        string="Sender country",
        comodel_name="res.country",
        required=True,
    )

    s_state_id = fields.Many2one(
        string="Sender state",
        comodel_name="res.country.state",
        domain="[('country_id', '=', 'country_id')]",
    )

    s_city = fields.Char(string="Sender city")
    s_street = fields.Char(string="Sender street")
    s_house = fields.Char(size=5, string="Sender house")
    s_flat = fields.Integer(string="Sender flat")

    s_zip = fields.Char(size=7, string="Sender index")

    # recipient address fields
    recipient_id = fields.Many2one(
        string="Recipient",
        comodel_name='wms.user.address',
        domain="[('is_recipient', '=', True),('client_id', '=', client_id),]",
    )

    r_country_id = fields.Many2one(
        string="Recipient country",
        comodel_name="res.country",
        required=True,
    )

    r_state_id = fields.Many2one(
        string="Recipient state",
        comodel_name="res.country.state",
        domain="[('country_id', '=', 'country_id')]",
    )

    r_city = fields.Char(string="Recipient city")
    r_street = fields.Char(string="Recipient street")
    r_house = fields.Char(size=5, string="Recipient house")
    r_flat = fields.Integer(string="Recipient flat")

    r_zip = fields.Char(size=7, string="Recipient index")

    # looks like 0-Door 1-branch, default Door
    r_delivery_type = fields.Selection(
        selection=[
            ('0', 'Door'),
            ('1', 'Branch'),
        ],
        default='0',
        string="Delyvery type",
    )

    r_carrier_id = fields.Many2one(
        comodel_name="wms.carrier"
    )
    r_carrier_branch_id = fields.Many2one(
        comodel_name="wms.carrier.branch",
        domain="[('carrier_id', '=', r_carrier_id)]",
    )

    @api.onchange('sender_id')
    def _onchange_sender_id(self):
        """Fill the sender`s fields, when it`s changed and filled
                sender_id: wms.user.address, _inherit = "wms.address.mixin"
        """
        self.ensure_one()
        if self.sender_id:
            self.s_country_id = self.sender_id.country_id.id
            self.s_state_id = self.sender_id.state_id.id
            self.s_city = self.sender_id.city
            self.s_street = self.sender_id.street
            self.s_house = self.sender_id.house
            self.s_flat = self.sender_id.flat
            self.s_zip = self.sender_id.zip

    @api.onchange('recipient_id')
    def _onchange_recipient_id(self):
        """Fill the recipient`s fields, when it`s changed and filled
                recipient_id: wms.user.address, _inherit = "wms.address.mixin"
        """
        self.ensure_one()
        if self.recipient_id:
            self.r_country_id = self.recipient_id.country_id.id
            self.r_state_id = self.recipient_id.state_id.id
            self.r_city = self.recipient_id.city
            self.r_street = self.recipient_id.street
            self.r_house = self.recipient_id.house
            self.r_flat = self.recipient_id.flat
            self.r_zip = self.recipient_id.zip
            self.r_carrier_id = self.recipient_id.carrier_id
            self.r_carrier_branch_id = self.recipient_id.carrier_branch_id
