from django.conf.urls import url
from usuarios import views

urlpatterns = [
    url(r'^usuarios/$', views.usuario_list),
    url(r'^usuarios/(?P<pk>[0-9]+)/$', views.usuario_detail),
]