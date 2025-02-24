from django.contrib import admin
from django.urls import path

from web.views import main_view, registration_view, login_view, logout_view, order_edit_view

urlpatterns = [
    path("", main_view, name="main"),
    path("registration/", registration_view, name="registration"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("orders/add/", order_edit_view, name="orders_add"),
    path("orders/<int:id>/", order_edit_view, name="orders_edit"),
]

