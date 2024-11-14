

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='room'),
    path('form_valid', views.form_valid, name='form_valid'),
]
