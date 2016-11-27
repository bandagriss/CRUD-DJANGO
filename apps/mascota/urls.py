from django.conf.urls import url, include

from apps.mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete, vacuna_list, vacuna_create, vacuna_delete, vacuna_edit

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', mascota_view, name='mascota_crear'),
    url(r'^listar$', mascota_list, name='mascota_listar'),
    url(r'^editar/(?P<id_mascota>\d+)/$', mascota_edit, name='mascota_editar'),
    url(r'^eliminar/(?P<id_mascota>\d+)/$', mascota_delete, name='mascota_eliminar'),
    url(r'^vacunas/listar$', vacuna_list, name='vacuna_listar'),
    url(r'^vacunas/nuevo$', vacuna_create, name='vacuna_crear'),
    url(r'^vacunas/editar/(?P<id_vacuna>\d+)/$', vacuna_edit, name='vacuna_editar'),
    url(r'^vacunas/eliminar/(?P<id_vacuna>\d+)/$', vacuna_delete, name='vacuna_eliminar'),

]
