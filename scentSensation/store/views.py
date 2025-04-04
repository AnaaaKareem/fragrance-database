from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse(render(request, 'store/homepage.html'))

def signAccount(request):
    return HttpResponse(render(request, 'store/account.html'))

def accountInformation(request):
    return HttpResponse(render(request, 'store/accountInfo.html'))

def store(request):
    return HttpResponse(render(request, 'store/storepage.html'))

def basket(request):
    return HttpResponse(render(request, 'store/basket.html'))