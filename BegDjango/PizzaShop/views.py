from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect, reverse
from .models import PizzaMenu, PizzaRecepts, Users, PizzaOrders
from .forms import Pizza, Authorization


def addPizzaSell(request, id):
    name = PizzaMenu.objects.get(pk=id).name
    cost = PizzaMenu.objects.get(pk=id).cost
    login = request.COOKIES.get('login')
    if PizzaOrders.objects.filter(name=name).exists():
        pizza = PizzaOrders.objects.get(name=name)
        pizza.count += 1
        pizza.save()
    else:
        PizzaOrders.objects.create(name=name, cost=cost, count=1, login=login)
    return redirect('menu')


def sellBag(request):
    if request.method == 'GET':
        login = request.COOKIES.get('login')
        login_status = request.COOKIES.get('login_status')
        role = request.COOKIES.get('role')
        menu = PizzaOrders.objects.filter(login=login).order_by('name')
        cost = 0
        for pizza in menu:
            cost += pizza.count * pizza.cost
        context = {
            'menu': menu,
            'login': login,
            'login_status': login_status,
            'role': role,
            'cost': cost
        }
        return render(request, 'sellbag/pizzaOrders.html', context=context)


def change_count_pizza_plus(request, id):
    pizza = PizzaOrders.objects.get(pk=id)
    pizza.count += 1
    pizza.save()
    return redirect('sellBag')


def change_count_pizza_minus(request, id):
    pizza = PizzaOrders.objects.get(pk=id)
    pizza.count -= 1
    pizza.save()
    return redirect('sellBag')

def pizzaMenu(request):
    if request.method == 'GET':
        menu = PizzaMenu.objects.all()
        login = request.COOKIES.get('login')
        login_status = request.COOKIES.get('login_status')
        role = request.COOKIES.get('role')
        context = {
            'menu': menu,
            'login': login,
            'login_status': login_status,
            'role': role
        }
        return render(request, 'mainPage/pizzaMenu.html', context=context)


def authorization(request):
    if request.method == "GET":
        return render(request, 'auth/auth.html')

    if request.method == "POST":
        login = request.POST.get('login')
        password = request.POST.get('password')
        if Users.objects.filter(login=login).exists() and Users.objects.filter(password=password).exists():
            role = Users.objects.get(login=login).role
            response = redirect('menu')
            response.set_cookie('login', login)
            response.set_cookie('login_status', True)
            response.set_cookie('role', role)
            return response
        else:
            return HttpResponse('Неверный пароль или логин')


def registration(request):
    if request.method == "GET":
        return render(request, 'reg/reg.html')

    if request.method == "POST":
        login = request.POST.get('login')
        password = request.POST.get('password')
        if Users.objects.filter(login=login).exists():
            return HttpResponse('Такой пользователь существует!')
        else:
            Users.objects.create(login=login, password=password)
            return HttpResponseRedirect('/auth')


def logout(request):
    response = HttpResponseRedirect(reverse('authorization'))
    response.delete_cookie('login')
    response.delete_cookie('login_status')
    return response


def addPizza(request):
    form = Pizza()
    if request.method == 'POST':
        form = Pizza(request.POST)
        if form.is_valid() and len(PizzaMenu.objects.filter(name=request.POST.get('name'))) == 0:
            PizzaMenu.objects.create(name=form.cleaned_data['name'], cost=form.cleaned_data['cost'])
            return redirect('menu')
        else:
            return HttpResponse('Такая пицца существует')
    context = {
        'form': form
    }
    return render(request, 'addPizza/addPizza.html', context=context)


def updatePizza(request, id):
    pizza = PizzaMenu.objects.get(pk=id)
    form = Pizza(instance=pizza)
    if request.method == 'POST':
        form = Pizza(request.POST, instance=pizza)
        if form.is_valid():
            form.save()
            return redirect('menu')
    context = {
        'form': form
    }
    return render(request, 'updatePizza/updatePizza.html', context=context)


def deletePizza(request, id):
    pizza = PizzaMenu.objects.get(pk=id)
    pizza.delete()
    return redirect('menu')


def deletePizzaOrder(request, id):
    pizza = PizzaOrders.objects.get(pk=id)
    pizza.delete()
    return redirect('sellBag')