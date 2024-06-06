{
    'name': 'Test Website',
    'category': 'Website/Theme',
    'version': '17.0.1.0.0',
    'author': 'Odoo PS',
    'depends': [
        'website',
    ],
    'license': 'OEEL-1',
    'data': [
        "data/website.xml",
        "data/assets.xml"
    ],
    "assets": {
        "web.assets_frontend": [
            # These assets are shared for all frontend
            "website_test/static/src/test_shared.js",
        ]
    }
}
