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
        'sequrity/ir.model.access.csv',
        'data/wms_data.xml',
        'views/wms__main__menu.xml',
        'views/wms_carrier_views.xml',
        'views/wms_carrier_branch_views.xml',
        'views/wms_country_views.xml',
        'views/wms_client_views.xml',
        'views/wms_package_views.xml',
        'views/wms_warehouse_views.xml',
        'views/wms_package_status_views.xml',
    ],
    'demo': [

    ],

    'installable': True,
    'auto_install': False,
    'application': False,

    'images': [
        'static/description/icon.png',
    ],

    'price': 0,
    'currency': 'EUR',
}
