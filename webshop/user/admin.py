# Register your models here.
from django.contrib import admin
from .models import *


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    class Meta:
        model = User

admin.site.register(User, UserAdmin)