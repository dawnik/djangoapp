from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns = [
    url('dupa', views.index, name='index'),
    path('register/', views.register_view, name='register_view', )
]