from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
def index(request):
    product = Product.objects.all()
    return render(request, 'main/index.html', {'product': product})

def man(request):
    return render(request, 'main/man.html')

def woman(request):
    return render(request, 'main/woman.html')

def child(request):
    return render(request, 'main/child.html')

def basket(request):
    return render(request, 'main/basket.html')
