from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^menu/$', views.menu),
    url(r'^routes/$', views.routes),
]
