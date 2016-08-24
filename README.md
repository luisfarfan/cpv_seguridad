# inei_django_example

Ejemplo del uso de Django y Django Rest Framework, para una aplicacion basada en RESTFULL.

Librerias usadas en este ejemplo:

* [django-pyodbc-azure==1.10.0.1] -
* [djangorestframework==3.4.4] -
* [pyodbc] -

### Installation
inei_django_example requiere de Django 1.8+
* Instalar las dependencias de *requirements.txt* que se encuentra en la raiz del proyecto. Se recomienda usar virtualenv.

```sh
$ pip install -r requirements.txt
```

* Colocar la configuracion de su base de datos en el archivo *settings.py*

```python
DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'TU BASE DE DATOS',
        'USER': 'TU USUARIO',
        'PASSWORD': 'TU CLAVE',
        'HOST': 'TU SERVIDOR',
        'PORT': 'TU PUERTO',

        'OPTIONS': {
            'driver': 'SQL Server',
        },
    },
}
```

* Luego, correr las migraciones.
```sh
$ python manage.py makemigrations seguridad
$ python manage.py migrate seguridad
```

* Por ultimo, correr tu aplicacion.
```sh
$ python manage.py runserver TUIP:TUPUERTO

```

Si todo esta correcto, ingresa a:
[http://TUIP:TUPUERTO/api/v1](http://TUIP:TUPUERTO/api/v1)


License
----
MIT

**Free Software, Hell Yeah!**
