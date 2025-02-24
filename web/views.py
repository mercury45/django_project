from django.contrib.auth import get_user_model, authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.datetime_safe import datetime

from web.forms import RegistrationForm, AuthForm, OrderForm
from web.models import Order

User = get_user_model()


# Create your views here.
def main_view(request):
    orders = Order.objects.all()
    return render(request, 'web/main.html', {
        "orders": orders
    })

def registration_view(request):
    form = RegistrationForm()
    is_success = False
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = User(
                username = form.cleaned_data['username'],
                email = form.cleaned_data['email'],
            )
            user.set_password(form.cleaned_data['password'])
            user.save()
            is_success = True
            print(form.cleaned_data)
    return render(request, 'web/registration.html', {
        "form" : form,
        "is_success" : is_success,
    })


def login_view(request):
    form = AuthForm()
    if request.method == 'POST':
        form = AuthForm(data=request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is None:
                form.add_error(None, 'Введены неверные данные')
            else:
                login(request, user)
                return redirect("main")
    return render(request, 'web/auth.html', {"form":form})


def logout_view(request):
    logout(request)
    return redirect("main")


def order_edit_view(request, id=None):
    order = None
    if id is not None:
        order = Order.objects.get(id=id)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(data=request.POST, files=request.FILES, instance=order,initial={"user": request.user})
        if form.is_valid():
            form.save()
            return redirect("main")
    return render(request, 'web/order_add_form.html', {
        "form": form
    })