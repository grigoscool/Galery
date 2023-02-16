from django.contrib import admin

from .models import Item, Photo


class PhotoInline(admin.StackedInline):
    model = Photo


class ItemAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]


admin.site.register(ItemAdmin, Item)
admin.site.register(Photo)
