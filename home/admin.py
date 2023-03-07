from django.contrib import admin
from .models import GalleryArt

class ListGalleryArt(admin.ModelAdmin):
    list_display = ('id','title', 'date_create')
    list_display_links = ('id','title', 'date_create',)
    list_per_page = 10

admin.site.register(GalleryArt, ListGalleryArt)
