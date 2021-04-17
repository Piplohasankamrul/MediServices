from django.contrib import admin
from .models import *
# Register your models here.

class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['product','user','quantity','price','amount','image_tag']
    list_filter = ['user']
    list_per_page = 10
    #search_fields = ['title','new_price','detail']
    #inlines = [productImageInline]
    #prepopulated_fields = {'slug':('title',)}
admin.site.register(ShopCart,ShopCartAdmin)

class OrderProductline(admin.TabularInline):
    model = OderProduct
    fields = ('user', 'product', 'price', 'quantity', 'amount')
    #can_delete = False
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',
                    'phone', 'total', 'status', 'transaction_id']
    list_filter = ['status']
    fields = ('user', 'first_name', 'last_name',
                       'phone', 'address', 'city', 'country', 'total', 'ip', 'transaction_id')
    #can_delete = False
    inlines = [OrderProductline]


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'price', 'quantity', 'amount','image_tag']
    list_filter = ['user']


admin.site.register(Order, OrderAdmin)

admin.site.register(OderProduct, OrderProductAdmin)




