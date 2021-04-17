from django.urls import path
from .import views
urlpatterns = [
    path('ambulanceHome/', views.ambulanceHome,name ='ambulanceHome'),
    path('Ambulance_register/', views.Ambulance_register,name ='Ambulance_register'),
    path('ambulance/<int:id>/', views.ambulance_single_profile,name ='ambulance_single_profile'),
    path('ambulance/<int:id>/<slug:slug>/', views.category_ambulance,name ='category_ambulance'),

]