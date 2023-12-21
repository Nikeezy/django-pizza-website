from . import views
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.pizzaMenu, name='menu'),
    path('sellBag', views.sellBag, name='sellBag'),
    path('addPizza', views.addPizza, name='addPizza'),
    path('<int:id>/changeCountPlus', views.change_count_pizza_plus, name='updateCountPlus'),
    path('<int:id>/changeCountMinus', views.change_count_pizza_minus, name='updateCountMinus'),
    path('<int:id>/addSell', views.addPizzaSell, name='addPizzaSell'),
    path('<int:id>/update', views.updatePizza, name='updatePizza'),
    path('<int:id>/delete', views.deletePizza, name='deletePizza'),
    path('<int:id>/deleteOrder', views.deletePizzaOrder, name='deletePizzaOrder'),
    path('logout', views.logout, name='logout'),
    path('auth', views.authorization, name='authorization'),
    path('reg', views.registration, name='registration'),
    path('static/css/mainPage/mainPage.css',
         TemplateView.as_view(template_name='mainPage.css', content_type='text/css'))
]