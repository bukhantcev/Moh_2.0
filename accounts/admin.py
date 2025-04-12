from django.contrib import admin
from .models import Profile, Dolgnost, Podrazdelenie
# Register your models here.



admin.site.register(Podrazdelenie)

admin.site.register(Dolgnost)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'first_name', 'last_name', 'phone', 'podrazdelenie', 'dolgnost', 'status', 'sort_index', 'is_boss', 'is_bigboss',)
    list_editable = ('sort_index', 'is_boss', 'is_bigboss',)
    list_filter = ('dolgnost', 'podrazdelenie', 'sort_index',)