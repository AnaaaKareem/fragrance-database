from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Home Page')

def signAccount(request):
    return HttpResponse('Account Sign Page')

def accountInformation(request):
    return HttpResponse('Account Information')

def store(request):
    return HttpResponse('Store')

def basket(request):
    return HttpResponse('Basket Page')