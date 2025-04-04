from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='store-home'),
    path('', views.signAccount, name='store-account'),
    path('', views.accountInformation, name='store-accountInfo'),
    path('', views.store, name='store-page'),
    path('', views.basket, name='store-basket')
]