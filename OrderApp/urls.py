from django.urls import path
from .import views

urlpatterns = [
    path('add_to_shop_cart/<int:id>/', views.add_to_shop_cart, name='add_to_shop_cart'),
    path('cart_detials/', views.cart_detials, name='cart_detials'),
    path('cart_delete/<int:id>/', views.cart_delete, name='cart_delete'),
    path('oder_cart/', views.OrderCart, name='OrderCart'),
    path('orderlist/', views.Order_showing, name="orderlist"),
    path('OrderProduct/', views.Order_Product_showing, name="orderproduct"),
    path('OrderDetails/<int:id>/', views.user_oder_details, name="user_oder_details"),
    path('OrderProductDetails/<int:id>/<int:oid>/', views.useroderproduct_details, name="useroderproduct_details"),
]