from django.shortcuts import render
from django.http import HttpResponse

from .models import MenuItem
# Create your views here.

def index(request):
    return render(request, 'mainpage/index.html')

def menu(request):
    fullMenu = MenuItem.objects.all()
    context = {
        'menu': fullMenu
    }
    return render(request, 'mainpage/LunchMenu.html', context)