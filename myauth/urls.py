from django.conf.urls import url
from .views import log_out, auth, register


urlpatterns = [
    url(r'^$', auth, name='auth'),
    url(r'^logout/$', log_out, name='logout'),
    url(r'^registration/$', register, name='register')
]