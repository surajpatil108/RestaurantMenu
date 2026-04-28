from django.urls import path
from . import views

app_name = "menu"

urlpatterns = [
    path("", views.menu_list, name="menu_list"),
    path("order/", views.order_page, name="order_page"), # New URL
]