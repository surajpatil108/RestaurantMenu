from django.shortcuts import render

# Create your views here.
from .models import Category, MenuItem

def menu_list(request):
    categories = Category.objects.prefetch_related("menuitem_set").all()
    return render(request, "menu/menu_list.html", {"categories": categories})

def order_page(request):
    # For now, we'll just show the page. 
    # Later you can pass the menu items here to create a checkout.
    categories = Category.objects.prefetch_related("menuitem_set").all()
    return render(request, "menu/order_page.html", {"categories": categories})