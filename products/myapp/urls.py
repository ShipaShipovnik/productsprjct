from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('order_form', views.order_form, name='orderform'),
    path('cust_form', views.cust_form, name='custform'),
    path('prod_form', views.prod_form, name='prodform'),
    path('products', views.products, name='products'),
    path('customers', views.customers, name='customers'),

]
