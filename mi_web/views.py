from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic import DateDetailView
from django.views.generic import ListView, DetailView, TemplateView, View
from mi_web.models import  Herramientas, Proveedores,Repuestos,Cliente, Accesorios, Reparacion , Reparacion
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django_xhtml2pdf.views import PdfMixin
from django_xhtml2pdf.utils import pdf_decorator
from django.db.models import Q
from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponse
from django.core.paginator import Paginator



def home(request):
    return render(request,'index.html')


def buscar(request):
    if 'q' in request.GET:
        q = request.GET['q']
        all_reparacion_list = Reparacion.objects.filter(Q(cliente__icontains=q)).order_by('cliente',
        Q(imei__icontains=q)).order_by('imei')
    else:
        all_reparacion_list = Reparacion.objects.all().order_by('cliente')
        all_reparacion_list = Reparacion.objects.all().order_by('imei')

    paginator = Paginator(all_reparacion_list, 2)        #revisar codigo hasta que sea correcto el Paginator
    page = request.GET.get('page')   
    all_ingresos = paginator.get_page(page)

    return render(request, 'buscar.html', {"reparacion":all_reparacion_list})


class About(TemplateView):
    template_name = "about.html"

class InventarioTaller(TemplateView):
    template_name = "inventario_taller.html"

class Contacto(TemplateView):
    template_name = "contacto.html"


class ListarClientes(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = "listar_clientes.html"


class ListarProveedores(LoginRequiredMixin,ListView):
    model = Proveedores
    template_name = "listar_proveedores.html"
    context_object_name = 'proveedores'


class ListarAccesorios(LoginRequiredMixin,ListView):
    model = Accesorios
    template_name = "listar_accesorios.html"


class ListarRepuestos(LoginRequiredMixin,ListView):
    model = Repuestos
    template_name = "listar_repuestos.html"


class ListarHerramientas(LoginRequiredMixin,ListView):
    model = Herramientas
    template_name = "listar_herramientas.html"    


class CrearCliente(LoginRequiredMixin,CreateView):
    model = Cliente
    template_name = "crear_cliente.html"
    success_url = 'listar-clientes'
    fields = ['nombre','apellido','telefono']


class CrearProveedor(LoginRequiredMixin,CreateView):
    model = Proveedores
    template_name = "crear_proveedor.html"
    success_url = 'listar-proveedores'
    fields = ['nombre','telefono']


class CrearRepuesto(LoginRequiredMixin,CreateView):
    model = Repuestos
    template_name = "crear_repuesto.html"
    success_url = 'listar-repuestos'
    fields = ['clase','marca','modelo', 'precio', 'stock']


class CrearHerramienta(LoginRequiredMixin,CreateView):
    model = Herramientas
    template_name = "crear_herramienta.html"
    success_url = 'listar-herramientas'
    fields = ['clase','marca','precio', 'stock']


class CrearAccesorio(LoginRequiredMixin,CreateView):
    model = Accesorios
    template_name = "crear_accesorio.html"
    success_url = 'listar-accesorios'
    fields = ['clase','marca','modelo', 'precio', 'stock']


class EditarCliente(LoginRequiredMixin,UpdateView):
    model = Cliente
    template_name ='editar_cliente.html'
    success_url = reverse_lazy('listar_clientes')
    fields = ['nombre','apellido','telefono']  


class EditarProveedor(LoginRequiredMixin,UpdateView):
    model = Proveedores
    template_name = "editar_proveedor.html"
    success_url = reverse_lazy('listar_proveedores')
    fields = ['nombre','telefono']


class EditarAccesorio(LoginRequiredMixin,UpdateView):
    model = Accesorios
    template_name = 'editar_accesorio.html'
    success_url = reverse_lazy('listar_accesorios')
    fields = ['clase','marca','modelo', 'precio', 'stock']


class EditarRepuesto(LoginRequiredMixin,UpdateView):
    model = Repuestos
    template_name = "editar_repuesto.html"
    success_url = reverse_lazy('listar_repuestos')
    fields = ['clase','marca','modelo', 'precio', 'stock']


class EditarHerramienta(LoginRequiredMixin,UpdateView):
    model = Herramientas
    template_name = "editar_herramienta.html"
    success_url = reverse_lazy('listar_herramientas')
    fields = ['clase','marca','precio', 'stock']


class EliminarCliente(LoginRequiredMixin,DeleteView):
    model = Cliente
    template_name = "eliminar_cliente.html"
    success_url = reverse_lazy('listar_clientes')


class EliminarProveedor(LoginRequiredMixin,DeleteView):
    model = Proveedores
    template_name = "eliminar_proveedor.html"
    success_url = reverse_lazy('listar_proveedores')


class EliminarAccesorio(LoginRequiredMixin,DeleteView):
    model = Accesorios
    template_name = "eliminar_accesorio.html"
    success_url = reverse_lazy('listar_accesorios')
    
    
class EliminarRepuesto(LoginRequiredMixin,DeleteView):
    model = Repuestos
    template_name = "eliminar_Repuesto.html"
    success_url = reverse_lazy('listar_repuestos')


class EliminarHerramienta(LoginRequiredMixin,DeleteView):
    model = Herramientas
    template_name = "eliminar_herramienta.html"
    success_url = reverse_lazy('listar_herramientas')


class MostrarCliente(LoginRequiredMixin,DetailView):
    model = Cliente
    template_name = 'mostrar_cliente.html'
    

class MostrarProveedor(LoginRequiredMixin,DetailView):
    model = Proveedores
    template_name = "mostrar_proveedor.html"
    

class MostrarAccesorio(LoginRequiredMixin,DetailView):
    model = Accesorios
    template_name = "mostrar_accesorio.html"
   

class MostrarRepuesto(LoginRequiredMixin,DetailView):
    model = Repuestos
    template_name = "mostrar_repuesto.html"
   
    

class MostrarHerramienta(LoginRequiredMixin,DetailView):
    model = Herramientas
    template_name = "mostrar_herramienta.html"
    
@pdf_decorator
def render_template_decorated(request):
    return render(request, 'impresiones.html')


class MostrarIngreso(PdfMixin, DetailView):
    model = Reparacion
    template_name = "mostrar_ingreso.html"


class ListarIngresos(LoginRequiredMixin, ListView):
    model = Reparacion
    template_name = "listar_ingresos.html"


class CrearIngreso(LoginRequiredMixin,CreateView):
    model = Reparacion
    template_name = "crear_ingreso.html"
    success_url = 'listar-ingresos'
    fields = ['cliente','telefono', 'marca','modelo', 'imei', 'falla',
    'imagen', 'comentarios', 'presupuesto' ,'precio', 'estado']


class EditarIngreso(LoginRequiredMixin,UpdateView):
    model = Reparacion
    template_name = 'editar_ingreso.html'
    success_url = reverse_lazy('listar_ingresos')
    fields = ['cliente','telefono', 'marca','modelo', 'imei', 'falla',
    'imagen', 'comentarios', 'presupuesto' ,'precio', 'estado']

class EliminarIngreso(LoginRequiredMixin,DeleteView):
    model = Reparacion
    template_name = "eliminar_ingreso.html"
    success_url = reverse_lazy('listar_ingresos')

class MostrarReparacion(LoginRequiredMixin, DetailView):
    model = Reparacion
    template_name = "mostrar_ingreso.html"
