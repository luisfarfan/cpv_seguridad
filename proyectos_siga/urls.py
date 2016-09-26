from django.conf.urls import url
from proyectos_siga import views

urlpatterns = [
    url(r'^proyectos_siga/$', views.proyectossiga_list),
    url(r'^proyectos_siga/(?P<pk>[0-9]+)/$', views.proyectossiga_detail),
]
