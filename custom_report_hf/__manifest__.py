# pylint: disable=missing-docstring, manifest-required-author
{
    'name': 'Custom Report Header/Footer',
    'summary': 'Custom Report Header/Footer',
    'description': "Custom All Reports in Odoo and add new header and footer based on multi company  - Odoo Reporting",
    'license': 'LGPL-3',
    'author': 'Ahmed Hegazy, Samah Kandil,Python and Odoo developers',
    'website':"linkedin.com/in/ahmedhegazy1995/linkedin.com/in/samah-kandil-odoo/",
    'category': 'tools',
    'images':['static/description/main_photo.jpeg'],
    'version': '13.0.1.0.1',
    'price': 14.99,
    'currency': 'USD',
    'depends': [
        'base',
    ],
    'data': [
        'report/custom_layout.xml',
        'views/res_company_views.xml',
    ],
    'demo': [

    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
