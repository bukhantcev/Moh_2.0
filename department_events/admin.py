from django.contrib import admin
from .models import (
    DepartmentEvent,
    DepartmentEventType,
    DepartmentEventName,
    DepartmentEventLocation
)

@admin.register(DepartmentEvent)
class DepartmentEventAdmin(admin.ModelAdmin):
    list_display = ('datetime', 'type', 'name', 'location', 'department')
    filter_horizontal = ('staff',)

@admin.register(DepartmentEventType)
class DepartmentEventTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')

@admin.register(DepartmentEventName)
class DepartmentEventNameAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')

@admin.register(DepartmentEventLocation)
class DepartmentEventLocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')
