from django.urls import path
from .import views

urlpatterns = [
    path('medihome/', views.medihome,name ='medihome'),
    path('product/<int:id>/', views.product_single_profile,name ='product_single_profile'),
    path('product/<int:id>/<slug:slug>/', views.category_product,name ='category_product'),
    path('about/', views.About,name ='About'),
    path('contact/', views.Contact,name ='Contact'),
    path('search/', views.SearchView,name ='SearchView'),

    #path('add_to_shop_cart/', views.add_to_shop_cart,name ='add_to_shop_cart'),


]
