from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Company)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('company', 'name', 'email', 'address', 'phone', 'description',)
    search_fields = ('company', 'name',)
    list_filter = ('company', 'name', 'phone',)


admin.site.register(Post)

