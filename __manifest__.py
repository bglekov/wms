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
        'views/wms__main__menu.xml',
        'views/wms_carrier_views.xml',
        'views/wms_country_views.xml',
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
