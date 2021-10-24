from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='ecomPages-home'),
    path('contact/', views.contact, name='ecomPages-contact'),
    path('products/', views.allproducts, name='ecomPages-products'),
    path('leathers/', views.allproducts, name='ecomPages-leather_typeA'),
]