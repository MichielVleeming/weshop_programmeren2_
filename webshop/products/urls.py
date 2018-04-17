from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:product_id>/', views.detail, name='detail'),
    path('order/', views.order, name='order'),
    path('signup', views.signup, name='signup')
]