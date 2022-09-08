from django.contrib import admin
from mi_web.models import  Accesorios,Repuestos,Proveedores,Cliente,  Herramientas, IngresoTecnico , Reparacion


admin.site.register(IngresoTecnico)
admin.site.register(Repuestos)
admin.site.register(Proveedores)
admin.site.register(Cliente)
admin.site.register(Accesorios)
admin.site.register(Herramientas)
admin.site.register(Reparacion)
