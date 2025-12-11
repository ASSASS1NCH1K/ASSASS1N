from django.contrib import admin
from .models import Sale, Car, Client, Dealer, Dealership

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'color', 'price')
    list_filter = ('brand', 'year', 'color')
    search_fields = ('brand', 'model')
    ordering = ('-year',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'email')
    search_fields = ('first_name', 'last_name', 'phone_number')
    ordering = ('last_name', 'first_name')


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'email')
    search_fields = ('first_name', 'last_name')
    ordering = ('last_name', 'first_name')


@admin.register(Dealership)
class DealershipAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', 'location')


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('car', 'client', 'dealer', 'sale_date', 'sale_amount')
    list_filter = ('sale_date', 'dealer', 'dealership')
    date_hierarchy = 'sale_date'
    ordering = ('-sale_date',)