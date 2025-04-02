from django.contrib import admin

from restaurant.models import Order, Table, TimeSection

# Register your models here.

admin.site.register(Order)
admin.site.register(Table)
admin.site.register(TimeSection)
