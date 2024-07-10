from odoo import api, models, fields

class pedidos(models.Model):
    _name = "pedidos"

    name = fields.Char('Folio')
    proveedor_id = fields.Many2one('proveedor', String='Proveedor')
    fecha_pedido = fields.Date(String = "Fecha de Pedido")
    estado_pago = fields.Selection([('Pagado','Pagado'),
                                    ('Pendiente','Pendiente')],String = 'Estado de Pago')
    pedidos_detalles_ids = fields.One2many('pedidos.detalles', 'pedidos_ids')
    monto_total = fields.Float(string="Monto Total a Pagar", compute="_compute_monto_total", store=True)

    def create(self,vals):
        vals['estado_pago']= 'Pendiente'
        return super(pedidos,self).create(vals)

    @api.depends('pedidos_detalles_ids.precio')
    def _compute_monto_total(self):
        for pedido in self:
            total = sum(detalle.precio for detalle in pedido.pedidos_detalles_ids)
            pedido.monto_total = total

                    
    class pedidos_detalles (models.Model):
        _name = 'pedidos.detalles'

        pedidos_ids = fields.Many2one('pedidos', String='Pedidos')
        material_id = fields.Many2one('material', String='Materiales')
        cantidad = fields.Integer('Cantidad')
        precio = fields.Float('Precio')
        
