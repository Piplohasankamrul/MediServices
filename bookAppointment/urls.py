from django.urls import path
from .import views
urlpatterns = [
    path('base/', views.base,name ='base'),
    path('', views.finddoctor,name ='fiddoctor'),
    path('doctor/', views.doctor,name ='doctor'),
    path('doctor_profile/<int:id>/', views.doctor_profile,name ='doctor_profile'),
    path('bappointment/<int:id>/', views.bookappointment,name ='bappointment'),
    path('basic/', views.basic,name ='basic'),
    path('dlist/', views.doctorlist,name ='dlist'),
    path('books/', views.Booking_showing,name ='Booking_showing'),
    path('Doctor_Booking_showing/', views.Doctor_Booking_showing,name ='Doctor_Booking_showing'),
    path('appointment_delete/<int:id>/', views.appointment_delete,name ='appointment_delete'),
    path('user_appointment_delete/<int:id>/', views.user_appointment_delete,name ='user_appointment_delete'),
    #path('Doctor_Booking_status_change/', views.Doctor_Booking_status_change,name ='Doctor_Booking_status_change'),
    path('doctor_register/', views.Doctor_register,name ='Doctor_register'),
    #path('doctor_logIn/', views.doctor_logIn, name='doctor_logIn'),
    #path('afterlogin', views.afterlogin_view,name='afterlogin'),
    #path('doctorclick', views.doctorclick_view),
   # path('doctor_signUp/', views.doctor_signUp, name='doctor_signUp'),
    path('Appointment_Book/<int:id>/', views.Appointment_Book,name ='Appointment_Book'),
    path('category_doctor/<int:id>/<slug:slug>/', views.category_doctor,name ='category_doctor'),
    #path('doctor_show/', views.doctor_show_categorywise,name ='doctor_show_categorywise'),


]