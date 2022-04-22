from django.contrib import admin

from .models import *


class TovarAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_published")
    list_display_links = ("id", "title")
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Tovar, TovarAdmin)
admin.site.register(Category, CategoryAdmin)
