from django import forms

class PizzaForm(forms.Form):
    SIZES= [("small", "Small"), ("medium", "Medium"), ("large", "Large")]
    toppings = forms.MultipleChoiceField(choices=[('pap', "Paperoni"), ("cheese", "Cheese"), ("olivie", "Olivie")], widget=forms.CheckboxSelectMultiple)
    size = forms.ChoiceField(label="Size", choices=SIZES)
# from pizza.models import Pizza
#
#
# class PizzaForm(forms.ModelForm):
#     class Meta:
#         model = Pizza
#         fields = ("topping1", "topping2", "size")
#         labels = {"topping1": "Topping 1", "topping2": "Topping 2"}
