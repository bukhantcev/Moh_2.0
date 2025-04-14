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
    path('event-type/new', views.create_event_type, name='create_event_type'),
    path('event-name/new', views.create_event_name, name='create_event_name'),
    path('event-location/new', views.create_event_location, name='create_event_location'),
    path('edit_event/<int:event_id>/', views.edit_event, name='edit_event'),
    path('delete_event/<int:event_id>/', views.delete_event, name='delete_event'),
    path('update_event_date/<int:event_id>/', views.update_event_date, name='update_event_date'),
    path('event-type/', views.manage_event_types, name='manage_event_types'),
    path('event-type/edit/<int:pk>/', views.edit_event_type, name='edit_event_type'),
    path('event-type/delete/<int:pk>/', views.delete_event_type, name='delete_event_type'),
    path('event/<int:event_id>/assign_staff/', views.assign_event_staff, name='assign_event_staff'),

    path('event-name/', views.manage_event_names, name='manage_event_names'),
    path('event-name/edit/<int:pk>/', views.edit_event_name, name='edit_event_name'),
    path('event-name/delete/<int:pk>/', views.delete_event_name, name='delete_event_name'),

    path('event-location/', views.manage_event_locations, name='manage_event_locations'),
    path('event-location/edit/<int:pk>/', views.edit_event_location, name='edit_event_location'),
    path('event-location/delete/<int:pk>/', views.delete_event_location, name='delete_event_location'),
]
