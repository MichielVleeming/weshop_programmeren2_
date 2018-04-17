from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .models import Product


# Create your views here.

def index(request):
    product_list = Product.objects.order_by('-pub_date')
    context = {
        'product_list': product_list
    }
    return render(request, 'products/index.html', context)


def detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    context = {
        'product': product
    }
    return render(request, 'products/detail.html', context)


def order(request):
    return render(request, 'products/order.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('../products/')
    else:
        form = UserCreationForm()
    return render(request, 'products/signup.html', {'form': form})
