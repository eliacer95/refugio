from django.conf.urls import url, include
from apps.adopcion import views
urlpatterns = [
    url(r'^index$', views.index_adopcion),
    url(r'^solicitud/listar$', views.SolicitudList.as_view(), name='solicitud_listar'),
    url(r'^solicitud/nueva$', views.SolicitudCreate.as_view(), name='solicitud_crear'),
    url(r'^solicitud/editar/(?P<pk>\d+)$', views.SolicitudUpdate.as_view(), name='solicitud_editar'),
    url(r'^solicitud/eliminar/(?P<pk>\d+)$', views.SolicitudDelete.as_view(), name='solicitud_eliminar'),

]