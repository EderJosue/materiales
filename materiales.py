from odoo import api, fields, models

class materiales(models.Model):
    _name = 'material'

    name = fields.Char('Nombre', required = True)
    precio = fields.Monetary(string='Precio', currency_field='divisa') 
    divisa = fields.Many2one('res.currency', string='Divisa', default = 33, invisible = True)