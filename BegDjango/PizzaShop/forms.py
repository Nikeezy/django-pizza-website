from django import forms
from .models import PizzaMenu, Users


class Pizza(forms.ModelForm):
    class Meta:
        model = PizzaMenu
        fields = ['name', 'cost']


class Authorization(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['login', 'password']