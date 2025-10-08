from django.contrib import admin
from .models import Dealership
from .models import Car
from .models import Dealer
from .models import Client
from .models import Sale


admin.site.register(Dealership)
admin.site.register(Car)
admin.site.register(Dealer)
admin.site.register(Client)
admin.site.register(Sale)

