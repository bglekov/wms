from odoo.tests.common import TransactionCase


class TestCommon(TransactionCase):

    def setUp(self):
        super(TestCommon, self).setUp()
        self.wms_user = self.env.ref(
            'wms.wms_user')
        self.wms_admin = self.env.ref(
            'wms.wms_admin')
        self.test_wms_user = self.env['res.users'].create({
            'name': 'WMS User',
            'login': 'wms_user',
            'groups_id': [(4, self.env.ref('base.group_user').id),
                          (4, self.wms_user.id)],
        })
        self.test_wms_admin = self.env['res.users'].create({
            'name': 'WMS Admin',
            'login': 'wms_admin',
            'groups_id': [(4, self.env.ref('base.group_user').id),
                          (4, self.wms_admin.id)],
        })
        self.demo_carrier = self.env['wms.carrier'].create({'name': 'Demo carrier'})
        self.demo_carrier_branch = self.env['wms.carrier.branch'].create({
            'name': 'Demo carrier branch'})
        self.demo_package = self.env['wms.package'].create({'name': 'Demo package'})
        self.demo_package_status = self.env['wms.package.status'].create({'name': 'Demo status'})
        self.demo_user_address = self.env['wms.user.address'].create({'name': 'Demo address'})
        self.demo_warehouse = self.env['res.company'].create({'name': 'Demo warehouse'})
