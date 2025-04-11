from django.shortcuts import render
from .models import *

def home(request):
    return render(request, 'store/homepage.html')

def signinout(request):
    return render(request, 'store/account.html')

def account(request):
    return render(request, 'store/accountInfo.html')

def store(request):
    products = Products.objects.all()
    images = ProductImages.objects.all()
    return render(request, 'store/storepage.html', {'products': products, 'images': images})

def basket(request):
    basket = Basket.objects.all()
    return render(request, 'store/basket.html',{'basket': basket})