from django.shortcuts import render

def home(request):
    return render(request, 'ecomPages/home.html')

def allproducts(request):
    return render(request, 'ecomPages/allproducts.html')

def leather_typeA(request):
    return render(request, 'ecomPages/leather_typeA.html')

def contact(request):
    return render(request, 'ecomPages/contact.html')
