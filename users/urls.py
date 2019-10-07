from django.conf.urls import url
from . import views
from django.urls import re_path


urlpatterns = [
    re_path('', views.index, name='index'),
    re_path('register/', views.register_view, name='register_view', )
]