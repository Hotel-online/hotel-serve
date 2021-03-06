from django.contrib import admin
from hotel.models.reservacion import Reservacion
from hotel.models.categoria import Categoria
from hotel.models.habitacion import Habitacion
from hotel.models.detalleReservacion import DetalleReservacion
from hotel.models.pago import Forma_de_pago
from hotel.models.cliente import Cliente
from hotel.models.venta import Venta
from hotel.models.detalleVenta import DetalleVenta
from hotel.models.docType import Doc_Type


# Register your models here.
admin.site.register(Reservacion)
admin.site.register(Categoria)
admin.site.register(Habitacion)
admin.site.register(DetalleReservacion)
admin.site.register(Forma_de_pago)
admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
admin.site.register(Doc_Type)
