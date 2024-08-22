from django.contrib import admin
from . models import Equipment, Category
from django.utils.safestring import mark_safe


admin.site.site_header = 'Панель администрирования'


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'place', 'description', 'cat', 'tags', 'photo']
    # readonly_fields = ['photo']
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'place', 'description', 'time_create', 'time_update', 'slug', 'post_photo')
    ordering = ('-time_create', 'title')
    list_per_page = 5
    search_fields = ['title'] 

    @admin.display(description="Изображение")
    def post_photo(self, equipment: Equipment):
        if equipment.photo:
            return mark_safe(f"<img src='{equipment.photo.url}' width=50>")
        return "Без фото"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug')
    search_fields = ['title']

