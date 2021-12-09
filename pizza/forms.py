from django import forms
from pizza.models import Pizza, Size


# class PizzaForm(forms.Form):
#     SIZES= [("small", "Small"), ("medium", "Medium"), ("large", "Large")]
#     toppings = forms.MultipleChoiceField(choices=[('pap', "Paperoni"), ("cheese", "Cheese"), ("olivie", "Olivie")], widget=forms.CheckboxSelectMultiple)
#     size = forms.ChoiceField(label="Size", choices=SIZES)


class PizzaForm(forms.ModelForm):

    size = forms.ModelChoiceField(queryset=Size.objects, empty_label=None, widget=forms.RadioSelect)#CheckboxSelectMultiple
    image = forms.ImageField()

    class Meta:
        model = Pizza
        fields = ("topping1", "topping2", "size")
        labels = {"topping1": "Topping 1", "topping2": "Topping 2"}
        # widgets = {"size": forms.CheckboxSelectMultiple}
