{
    'name': 'Retana Home',
    'version': '16.0.1',
    'category': 'Tools',
    'summary': 'Custom Home Dashboard with App Cards',
    'description': """
        Custom Home Dashboard
        =====================
        
        This module provides a custom home dashboard that displays all installed
        applications as cards, similar to Odoo Enterprise home screen.
        
        Features:
        - View all installed apps as cards
        - Click to navigate to each app
        - Responsive design
        - Modern UI
    """,
    'author': 'MaxRetana',
    'website': 'https://github.com/MaxRetana',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/home_dashboard_views.xml',
        'views/menu_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'retana_home/static/src/css/home_dashboard.css',
            'retana_home/static/src/scss/navbar.scss',
            'retana_home/static/src/scss/main.scss',
            'retana_home/static/src/js/home_dashboard.js',
            'retana_home/static/src/xml/home_dashboard.xml',
            
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}