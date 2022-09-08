from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib import admin
from mi_web.views import ( home, ListarRepuestos, ListarClientes,
CrearCliente,  CrearHerramienta, CrearRepuesto,CrearProveedor,
EliminarCliente,EliminarHerramienta ,EliminarRepuesto,EditarCliente,   EditarHerramienta,
 EditarRepuesto, EditarProveedor,EliminarProveedor,
 EditarAccesorio,EliminarAccesorio,CrearAccesorio,ListarAccesorios,MostrarAccesorio,MostrarCliente, MostrarHerramienta,
  MostrarProveedor, MostrarRepuesto, InventarioTaller, ListarProveedores,ListarHerramientas,EliminarIngreso, 
  MostrarIngreso,EditarIngreso,CrearIngreso, ListarIngresos,  About, Contacto, buscar, MostrarReparacion )



urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('',home, name="index"),  
    path('listar-repuestos' , ListarRepuestos.as_view(), name='listar_repuestos'),
    path('listar-clientes' , ListarClientes.as_view(), name='listar_clientes'),
    path('listar-accesorios' , ListarAccesorios.as_view(), name='listar_accesorios'),
    path('listar-herramientas' , ListarHerramientas.as_view(), name='listar_herramientas'),
    path('listar-proveedores' , ListarProveedores.as_view(), name='listar_proveedores'),
    path('listar-ingresos' , ListarIngresos.as_view(), name='listar_ingresos'),

    path('contacto/', Contacto.as_view(), name="contacto"),
    path('about/', About.as_view(), name="about"),
    path('buscar/', buscar, name="buscar"),
    path('inventario-taller', InventarioTaller.as_view(), name="inventario_taller"),
    #path('admin' , admin.html'),
    #path('curso' , curso.html'),
    path('crear-cliente' , CrearCliente.as_view(), name='crear_cliente'),          
    path('crear-accesorio' , CrearAccesorio.as_view(), name='crear_accesorio'),     
    path('crear-herramienta' , CrearHerramienta.as_view(), name='crear_herramienta'),    
    path('crear-repuesto' , CrearRepuesto.as_view(), name='crear_repuesto'),        
    path('crear-proveedor' , CrearProveedor.as_view(), name='crear_proveedor'),    
    path('crear-ingreso' , CrearIngreso.as_view(), name='crear_ingreso'), 

    path('eliminar-cliente/<int:pk>' , EliminarCliente.as_view(), name='eliminar_cliente'),
    path('eliminar-accesorio/<int:pk>' , EliminarAccesorio.as_view(), name='eliminar_accesorio'),
    path('eliminar-herramienta/<int:pk>' , EliminarHerramienta.as_view(), name='eliminar_herramienta'),
    path('eliminar-repuesto/<int:pk>' , EliminarRepuesto.as_view(), name='eliminar_repuesto'),
    path('eliminar-proveedor<int:pk>' , EliminarProveedor.as_view(), name='eliminar_proveedor'),
    path('eliminar-ingreso<int:pk>' , EliminarIngreso.as_view(), name='eliminar_ingreso'),

    path('editar-cliente/<int:pk>' , EditarCliente.as_view(), name='editar_cliente'),
    path('editar-accesorio/<int:pk>' , EditarAccesorio.as_view(), name='editar_accesorio'),
    path('editar-herramienta/<int:pk>' , EditarHerramienta.as_view(), name='editar_herramienta'),
    path('editar-repuesto/<int:pk>' , EditarRepuesto.as_view(), name='editar_repuesto'),
    path('editar-proveedor/<int:pk>' , EditarProveedor.as_view(), name='editar_proveedor'),
    path('editar-ingreso/<int:pk>' , EditarIngreso.as_view(), name='editar_ingreso'),
    
    path('mostrar-cliente/<int:pk>/' , MostrarCliente.as_view(), name='mostrar_cliente'),
    path('mostrar-accesorio/<int:pk>/' , MostrarAccesorio.as_view(), name='mostrar_accesorio'),
    path('mostrar-herramienta/<int:pk>/' , MostrarHerramienta.as_view(), name='mostrar_herramienta'),
    path('mostrar-repuesto/<int:pk>/' , MostrarRepuesto.as_view(), name='mostrar_repuesto'),
    path('mostrar-proveedor/<int:pk>/' , MostrarProveedor.as_view(), name='mostrar_proveedor'),
    path('mostrar-ingreso/<int:pk>/' , MostrarIngreso.as_view(), name='mostrar_ingreso'),
    path('mostrar-reparacion/<int:pk>/' , MostrarReparacion.as_view(), name='mostrar_reparacion'),
   

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)