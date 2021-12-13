from django.contrib import admin
from django.urls import path

from pizza.views import home, order, pizzas

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name="home"),
    path('order/', order, name="order"),
    path('pizzas/', pizzas, name="pizzas"),
    path('pizzas/<pk>', pizzas, name="edit_order"),
]

