from django.contrib import admin

from .models import Category,Doctor,Product,Subcategory,Login
# Register your models here.


admin.site.register(Category)

admin.site.register(Doctor)

admin.site.register(Product)

admin.site.register(Subcategory)

admin.site.register(Login)