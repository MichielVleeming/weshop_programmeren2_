from django.contrib import admin
from .models import *


# Register your models here.

class ImageAdminInline(admin.TabularInline):
    model = Image


class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageAdminInline]

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
