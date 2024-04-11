{
    'name': 'SimpleWMS',
    'summary': 'WMS first try',

    'author': 'BoricH',
    'website': '',


    'category': 'Castomization',
    'license': 'OPL-1',
    'version': '17.0.0.0.1',

    'depends': [
        'base',
    ],

    'external_dependencies': {'python': [], },

    'data': [
        'security/wms_role_group.xml',
        'security/ir.model.access.csv',
        'data/wms_data.xml',
        'views/wms__main__menu.xml',
        # 'views/wms_arrive_views.xml',
        'views/wms_carrier_views.xml',
        'views/wms_carrier_branch_views.xml',
        'views/wms_country_views.xml',
        'views/wms_client_views.xml',
        'views/wms_user_address_views.xml',
        'views/wms_package_views.xml',
        'views/wms_warehouse_views.xml',
        'views/wms_package_status_views.xml',
        'report/wms_print_package_lable.xml',
        'wizard/wms_change_package_status_multi_wizard_view.xml'
    ],
    'demo': [
        'data/wms_demo_data.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': False,
    'images': ['static/description/icon.png'],
    'price': 0,
    'currency': 'EUR',
    'support': 'b.glekov@gmail.com',
}
