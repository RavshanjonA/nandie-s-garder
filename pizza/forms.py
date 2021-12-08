from django import forms


class PizzaForm(forms.Form):
    topping1 = forms.CharField(label="Topping 1", max_length=128)
    topping2 = forms.CharField(label="Topping 2", max_length=128)
    size = forms.ChoiceField(label="Size", choices=[("small", "Small"), ("medium", "Medium"), ("large", "Large")])
