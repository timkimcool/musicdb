from django.contrib import admin

from .models import AlbumBase, Review


class ReviewInline(admin.TabularInline):
    model = Review


class AlbumAdmin(admin.ModelAdmin):
    inlines = [ReviewInline,]
    list_display = ("name")


admin.site.register(AlbumBase, AlbumAdmin)
