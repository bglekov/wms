from odoo.addons.wms.tests.common import TestCommon
from odoo.tests import tagged
from odoo.exceptions import AccessError


@tagged('post_install', '-at_install', 'wms', 'access')
class TestAccessRights(TestCommon):

    def test_01_wms_user_access_rights(self):
        # test_wms_user create carrier
        with self.assertRaises(AccessError):
            self.env['wms.carrier'].with_user(self.test_wms_user).create(
                {'name': 'Test carrier'})
        # test_wms_admin unlink carrier
        with self.assertRaises(AccessError):
            self.demo_carrier.with_user(self.wms_admin).unlink()

        # test_wms_user create carrier branch
        with self.assertRaises(AccessError):
            self.env['wms.carrier.branch'].with_user(self.test_wms_user).create(
                {'name': 'Test carrier branch'})
        # test_wms_admin unlink carrier branch
        with self.assertRaises(AccessError):
            self.demo_carrier_branch.with_user(self.wms_admin).unlink()

    def test_02_wms_admin_access_rights(self):
        carrier = self.env['wms.carrier'].with_user(self.test_wms_admin).create(
            {'name': 'Test carrier'})
        carrier.with_user(self.test_wms_admin).read()
        carrier.with_user(self.test_wms_admin).write({'name': 'Test carrier 2'})
        carrier.with_user(self.test_wms_admin).unlink()

        carrier_branch = self.env['wms.carrier.branch'].with_user(self.test_wms_admin).create(
            {'name': 'Test carrier branch'})
        carrier_branch.with_user(self.test_wms_admin).read()
        carrier_branch.with_user(self.test_wms_admin).write({'name': 'Test carrier branch 2'})
        carrier_branch.with_user(self.test_wms_admin).unlink()
