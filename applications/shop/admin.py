from django.contrib import admin

from applications.shop.models import Item, Order

admin.site.register(Item)
admin.site.register(Order)
