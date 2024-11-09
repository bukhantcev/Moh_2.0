
from django.urls import path
from . import views

app_name = 'ajax'

urlpatterns = [
    path('First', views.FirstAjax, name='First'),
]

