from django.conf.urls import url
from apps.adopcion.views import index, new, edit, destroy

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^new$', new, name='new'),
    url(r'^edit/(?P<id_persona>\d+)/$', edit, name='edit'),
    url(r'^delete/(?P<id_persona>\d+)/$', destroy, name='delete'),
]
