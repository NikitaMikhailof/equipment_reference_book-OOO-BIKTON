from django.contrib import admin
from . models import Equipment, Category


admin.site.site_header = 'Панель администрирования'


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'place', 'description', 'cat', 'tags']
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'place', 'description', 'time_create', 'time_update', 'slug')
    ordering = ('-time_create', 'title')
    list_per_page = 5
    search_fields = ['title'] 


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    firlds = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug')
    search_fields = ['title']

