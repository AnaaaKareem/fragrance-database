from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('signup/', views.signup, name='signupAccount'),
    path('signin/', views.signin, name='signinAccount'),
    path('accountInfo/', views.account, name='accountInfo'),
    path('store/', views.store, name='store'),
    path('basket/', views.basket, name='basket')
]