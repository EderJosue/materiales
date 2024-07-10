from odoo import api, fields, models

class proveedor(models.Model):
    _name = 'proveedor'

    name = fields.Char('Nombre', required = True)
    calle = fields.Char('Calle')
    numero = fields.Char('Numero')
    colonia = fields.Char('Colonia')
    codigo_postal = fields.Char('Codigo Postal')
    telefono = fields.Char('Telefono')
    ciudad = fields.Char('Ciudad')

