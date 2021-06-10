from django.conf.urls import url
from .views import showdata, update, display

app_name = 'dappx'

urlpatterns = [
    url(r'^$', showdata, name='base'),
    url(r'^new/$', update, name='new'),
    url(r'^student/(?P<studentname>\w+)/$', display, name='student'),

]