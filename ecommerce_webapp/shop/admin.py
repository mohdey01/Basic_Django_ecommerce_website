from django.contrib import admin
from .models import Product,Contactus,Order,OrderUpdate
# Register your models here.

admin.site.register(Product)
admin.site.register(Contactus)
admin.site.register(Order)
admin.site.register(OrderUpdate)

