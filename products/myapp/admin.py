from django.contrib import admin

from .models import Orders, Customers, Products

admin.site.register(Products)
admin.site.register(Customers)
admin.site.register(Orders)
