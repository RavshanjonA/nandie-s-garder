from django.forms import formset_factory
from django.shortcuts import render, redirect
from django.contrib import messages

from pizza.forms import PizzaForm, MultiplePizzaForm
from pizza.models import Pizza


def home(request):
    return render(request, "pizza/home.html")


def order(request):
    multiple_form = MultiplePizzaForm()
    if request.method == "POST":
        form = PizzaForm(request.POST, request.FILES)
        if form.is_valid():
            created_pizza = form.save()
            created_pizza_pk = created_pizza.pk
            data = form.cleaned_data
            note = "Thanks for ordering, your  {1} and   {0} pizza on the way".format(data["size"], ", ".join(
                [data["topping1"], data["topping2"]]))
            # messages.success(request,"Your order was successfully added")
            form = PizzaForm()
            return render(request, "pizza/order.html",
                          context={"created_pizza_pk": created_pizza_pk, "form": form, "note": note,
                                   "multiple_form": multiple_form})
        else:
            messages.error(request, "Error saving form")
        return redirect("home")
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', context={"form": form, "multiple_form": multiple_form})


def pizzas(request):
    number_of_pizzas = 2
    filled_multiple_pizza_form = MultiplePizzaForm(request.GET)
    if filled_multiple_pizza_form.is_valid():
        number_of_pizzas = filled_multiple_pizza_form.cleaned_data["number"]

    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
    formset = PizzaFormSet()
    if request.method == "POST":
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data["topping1"])
            note = "Pizzas have been ordered"
        else:
            note = "Pizza was not created, please try again"
        return render(request, "pizza/pizzas.html", {"note": note, "formset": formset})
    else:
        return render(request, "pizza/pizzas.html", {"formset": formset})


def edit_order(request, pk):
    pizza = Pizza.objects.get(pk=pk)
    form = PizzaForm(instance=pizza)
    if request.method == "POST":
        filled_form = PizzaForm(request.POST, instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form

    return render(request, "pizza/edit_order.html", context={"pizzaform": form, "pizza": pizza})
