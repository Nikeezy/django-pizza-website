from django.contrib import admin
from .models import PizzaMenu, PizzaRecepts, Users, PizzaOrders


@admin.register(PizzaMenu)
class PizzaMenuAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'cost']
    list_editable = ['name', 'cost']


@admin.register(PizzaOrders)
class PizzaOrdersAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'cost', 'count', 'login']
    list_editable = ['name', 'cost', 'count', 'login']


@admin.register(PizzaRecepts)
class PizzaReceptsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'recept']
    list_editable = ['name', 'recept']


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['pk', 'login', 'password', 'role']
    list_editable = ['login', 'password', 'role']
