from django.contrib import admin
#from django.contrib.contenttypes.admin import GenericTabularInline
from applications.products.models import Product, ProductImage


#class ImageInline(GenericTabularInline):
    #model = ProductImage

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)

