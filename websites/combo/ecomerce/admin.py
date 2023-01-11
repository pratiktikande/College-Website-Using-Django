from django.contrib import admin
# from .models import Product
# from .models import order
from .models import Product,Orders

admin.site.register(Product)
admin.site.register(Orders)

# Register your models here.
