from django import forms
    

class FormCliente(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    telefono = forms.IntegerField()


class FormRepuestos(forms.Form):
    clase = forms.CharField(max_length=40)
    marca = forms.CharField(max_length=40)
    modelo = forms.CharField(max_length=40)
    precio = forms.IntegerField()
    stock = forms.IntegerField()


class FormAccesorios(forms.Form):
    clase = forms.CharField(max_length=40)
    marca = forms.CharField(max_length=40)
    modelo = forms.CharField(max_length=40)
    precio = forms.IntegerField()
    stock = forms.IntegerField()

class Herramientas(models.Model):
    clase = forms.CharField(max_length=40)
    marca = forms.CharField(max_length=40)
    precio = forms.IntegerField()    
    stock = forms.IntegerField()
    
class FormProveedores(forms.Form):
    nombre = forms.CharField(max_length=40)
    telefono = forms.CharField(max_length=40)
    


class FormPublisher(forms.Form):
    user = forms.ForeignKey(User, on_delete=forms.DO_NOTHING)
    avatar = forms.ImageField(upload_to="avatars", null=True, blank=True)
    fecha_creacion = forms.DateTimeField(auto_now_add=True)
    fecha_actual = forms.DateTimeField(auto_now=True)

    
class FormArticulo(forms.Form):
    titulo = forms.CharField(max_length=100)
    contenido_corto = forms.CharField(max_length=180)
    contenido = RichTextField()
    image = forms.ImageField(upload_to="articles", null=True, blank=True)
    autor = forms.ForeignKey(Publisher, on_delete=forms.DO_NOTHING)
    is_headline= forms.BooleanField()
    fecha_creacion = forms.DateTimeField(auto_now_add=True)
    fecha_actual = forms.DateTimeField(auto_now=True)
    fecha_publicacion = forms.DateTimeField()

class FormPortal(forms.Form):
    nombre = forms.CharField(max_length=20)
    red_social_uno = forms.URLField(null=True)
    red_social_dos = forms.URLField(null=True)
    email = forms.EmailField(null=True)
    fecha_creacion = forms.DateTimeField(auto_now_add=True)
    fecha_actual = forms.DateTimeField(auto_now=True)