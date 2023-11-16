from django.contrib import admin
from .models import New, Category, GalleryImage, Video
# Register your models here.

class NewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

class GalleryAdmin(admin.ModelAdmin):
    display = ('url')
    display_links = ('url')

class VideoAdmin(admin.ModelAdmin):
    display = ('image')
    display_links = ('image')

admin.site.register(Category, CategoryAdmin)
admin.site.register(New, NewAdmin)
admin.site.register(GalleryImage, GalleryAdmin)
admin.site.register(Video, VideoAdmin)
