from django.contrib import admin

from pizza.models import Size


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('name',)