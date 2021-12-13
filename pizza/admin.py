from django.contrib import admin

from pizza.models import Size, Pizza


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ("topping1", "topping2", "size")
