from django.contrib import admin
from .models import partner, product, stock
# Register your models here.

admin.site.register(partner)
admin.site.register(product)
admin.site.register(stock)
