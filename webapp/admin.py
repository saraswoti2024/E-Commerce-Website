from django.contrib import admin
from .models import *

# Register your models here.
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display=['id','title','brand_name','Category1','price','image']
admin.site.register([Category,Product])