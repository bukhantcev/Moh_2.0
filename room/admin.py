from django.contrib import admin
from .models import MyEvents, Type
# Register your models here.



@admin.register(MyEvents)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'date', 'time',)
    list_editable = ('date', 'time',)
    list_filter = ('date', 'user',)

@admin.register(Type)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ( 'name',)
