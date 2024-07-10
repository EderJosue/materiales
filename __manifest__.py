{
    'name': 'Gestion de notas para materiales',
    'version': '1.0',
    'summary': 'Gestion de notas para materiales',
    'description': 'Modulo que permite gestionar las notas por compras de materiales, dandole un seguimiento a los pagos',
    'author': 'Eder Josue Maldonado Gonzalez',
    'depends': ['base'],
    'data': [
        'views/materiales.xml',
        'views/pedidos_detalle.xml',
        'views/pedidos.xml',
        'views/proveedor.xml',
        'views/menu_view.xml'
    ],
    'installable': True,
    'auto_install': False,
}
