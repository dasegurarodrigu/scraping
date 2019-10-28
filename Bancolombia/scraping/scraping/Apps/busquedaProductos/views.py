from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import *;

def index(request):

    #error 403 csrf
    #search = request.POST.get('search')
    #print(search)


    latest_product_list = Product.objects.order_by('price')[:5]
  
    context = {
        'latest_product_list': latest_product_list,
    }
    return render(request, 'busquedaProductos/index.html', context)

