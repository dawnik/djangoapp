from django.conf.urls import url
from . import views


urlpatterns = [
    url('index', views.index, name='index'),
    url('register', views.register_view, name='register_view', )
]