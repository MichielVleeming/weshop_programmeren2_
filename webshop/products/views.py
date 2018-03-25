from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Product, Image


# Create your views here.

def index(request):
    product_list = Product.objects.order_by('-pub_date')
    context = {
        'product_list': product_list
    }
    return render(request, 'products/index.html', context)


def detail(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request, 'products/detail.html', {'product': product})
