from django.shortcuts import render

from pizza.forms import PizzaForm


def home(request):
    return render(request, "pizza/home.html")


def order(request):
    form = PizzaForm()
    return render(request, 'pizza/order.html', context={"form": form})
