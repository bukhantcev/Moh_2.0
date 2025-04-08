
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('spects', views.spects, name='spects'),
    path('add_spect', views.add_spect, name='add_spect'),
    path('edit_spect', views.edit_spect, name='edit_spect'),
    path('open_pdf', views.load_file, name='open_pdf'),
    path('folder', views.folder, name='folder'),
    path('workers', views.workers, name='workers'),
    path('add_event/', views.add_event, name='add_event'),
    path('edit_event/<int:event_id>/', views.edit_event, name='edit_event'),
    path('delete_event/<int:event_id>/', views.delete_event, name='delete_event'),
]

