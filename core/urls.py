from django.conf.urls import url
from django.urls import path
from core import views


urlpatterns = [
    path('', views.index, name='index')
]