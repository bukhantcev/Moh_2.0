from .views import (
    create_department_event, edit_dep_event, delete_dep_event,
    update_dep_event_date, add_type, add_name, add_location,
    manage_dep_event_types, manage_dep_event_names, manage_dep_event_locations,
    edit_dep_event_location, edit_dep_event_type, edit_dep_event_name, delete_dep_event_location,
    delete_dep_event_type, delete_dep_event_name, create_dep_event_type, create_dep_event_name, create_dep_event_location
)
from django.urls import path

urlpatterns = [
    path('create/', create_department_event, name='create_department_event'),
    path('edit_dep_event/<int:event_id>/', edit_dep_event, name='edit_dep_event'),
    path('delete_dep_event/<int:event_id>/', delete_dep_event, name='delete_dep_event'),
    path('update_dep_event_date/<int:event_id>/', update_dep_event_date, name='update_event_date'),
    path('add_type/', add_type, name='add_type'),
    path('add_name/', add_name, name='add_name'),
    # AJAX endpoint to add location from JS (POST only)
    path('add_location/', add_location, name='add_location'),
    path('manage_dep_event_types/', manage_dep_event_types, name='manage_dep_event_types'),
    path('manage_dep_event_names/', manage_dep_event_names, name='manage_dep_event_names'),
    path('manage_dep_event_locations/', manage_dep_event_locations, name='manage_dep_event_locations'),
    path('edit_dep_event_location/<int:pk>/', edit_dep_event_location, name='edit_dep_event_location'),
    path('edit_dep_event_type/<int:pk>/', edit_dep_event_type, name='edit_dep_event_type'),
    path('edit_dep_event_name/<int:pk>/', edit_dep_event_name, name='edit_dep_event_name'),
    path('dep_event-location/delete/<int:pk>/', delete_dep_event_location, name='delete_dep_event_location'),
    path('dep_event-type/delete/<int:pk>/', delete_dep_event_type, name='delete_dep_event_type'),
    path('dep_event-name/delete/<int:pk>/', delete_dep_event_name, name='delete_dep_event_name'),
    path('create_dep_event_type/', create_dep_event_type, name='create_dep_event_type'),
    path('create_dep_event_name/', create_dep_event_name, name='create_dep_event_name'),
    path('create_dep_event_location/', create_dep_event_location, name='create_dep_event_location'),
]
