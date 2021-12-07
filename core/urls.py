from django.contrib import admin
from django.urls import path

from pizza.views import home, order

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name="home"),
    path('order/', order, name="order"),
]
