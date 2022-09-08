# AdministradorST
                                              Plataforma de Administracion para Servicios Tecnicos
                                              
[!Deploy](https://heroku.com/deploy?template=https://github.com/Christian-Coria/AdministradorST)

[==> Casos de Prueba <==](https://docs.google.com/spreadsheets/d/1XS3uoYypWx3NZjh3MMgHA_54NBxl6aaDTBgHDIhAgvY/edit?usp=sharing)



## Este proyecto tiene como objetivo crear un sistema para la administración de Servicios Tecnicos de Telefonia Celular y afines.
Cosas que puedes hacer::

[==> Video de Funcionalidades <==](https://www.loom.com/share/1c1dcbb136da460ab3ceed488ec58dd9)

## Ingresar a los siguientes servicios previo Login:
- Crear, leer, actualizar y eliminar Clientes.
- Buscar Clientes en Base de Datos
- Crear, leer, actualizar y eliminar Reparaciones.
- Crear, leer, actualizar y eliminar Proveedores.
### Crear un inventario de los articulos del Taller:
- Crear, leer, actualizar y eliminar Accesorios.
- Crear, leer, actualizar y eliminar Herramientas.
- Crear, leer, actualizar y eliminar Herramientas.
### Area de ventas con las siguientes opciones previo login:
-- Nota: Wsta area requiere un diferente login y usuario.
- Publicacion de articulos.
- Busqueda de articulos.
- Login para registro como vendedor.
- Administrador de Vendedores.
### Area para Chat entre Usuarios :
-- Nota: Es necesario previamente acceder al administrador con el SuperUsuario y generar la salas de Chat.
### Area de recordatorios:
- Podras crear recordatorios asi como eliminarlos.
### Acceso previo Login a un Curso de Reparaciones:
- En este curso aprenderas tecnicas de reparacion en Fallas Reales de diferentes Modelos.


# Instalar

Para instalar este software necesitas:

## Comprobar la versión de Python
Este proyecto se escribió con Python 3.10.5, por lo que le sugiero que pruebe con esta versión o superior para no tener problemas de compatibilidad.

Cómo verifico mi versión de python,

en sistemas *nix: 

```bash
> python --version
> Python 3.8.0
```

en windows:

```bash
c:\> py --version
c:\> Python 3.8.0
```

## Instalar dependencias
Para instalar las dependencias, debe ejecutar `pip install`, asegúrese de estar en la carpeta del proyecto y pueda ver el 'requirements.txt' archivo cuando haga 'ls' o 'dir':

```bash
> pip install -r requirements.txt
```
Este último instalara los requerimientos necesarios en la terminal..

`algunos sistemas operativos requieren el uso de  pip3 o pip `

## Configuración de la aplicación Django

Una vez que termine la instalación de las dependencias, debe ejecutar algunos comandos Django.

### Migraciones

Initialize the database
:
```bash
> python mananage.py migrate
```
windows:
```bash
c:\> py mananage.py migrate
```

### Ejecutar el servidor de prueba

```bash
> python mananage.py runserver
```
windows:
```bash
c:\> py mananage.py runserver
```
Go to localhost:8000/

para tener acceso a la aplicación.

'Aclaracion: es necesario contar con internet par la carga de imagenes de templates.

Si todo va bien, debería poder abrir el navegador y ver cómo se ejecuta la aplicación.

### Futuras actualizaciones
En la proximas actualizaciones incluiremos:

- Busqueda por categorias de Reparacion, Accesorios y herramientas.




### 'EnLinea' Siempre a Tu Servicio.-                                                                                             © 2022 by Christian Coria