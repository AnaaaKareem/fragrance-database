from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('signup/', views.signup, name='signupAccount'),
    path('signin/', views.signin, name='signinAccount'),
    path('signout/', views.signout, name='signout'),
    path('account/', views.account, name='account'),
    path('store/', views.store, name='store'),
    path('basket/', views.basket, name='basket'),
    path('basket/delete/<int:product_id>/', views.delete_from_basket, name='delete_from_basket'),
    path('checkout/', views.checkout, name='checkout'),
]