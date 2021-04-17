from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name ='home'),
    path('doctorDashboard/',views.doctorDashboard,name ='doctorDashboard'),
    path('driverDashboard/',views.driverDashboard,name ='driverDashboard'),
    path('user_register/',views.user_register,name ='user_register'),
    path('doctor_register/',views.doctor_register,name ='doctor_register'),
    path('driver_register/',views.driver_register,name ='driver_register'),
    path('user_logIn/', views.user_logIn, name='user_logIn'),
    path('doctor_logIn/', views.doctor_logIn, name='doctor_logIn'),
    path('driver_logIn/', views.driver_logIn, name='driver_logIn'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('doctor_logout/', views.doctor_logout, name='doctor_logout'),
    path('driver_logout/', views.driver_logout, name='driver_logout'),
    path('user_profile/', views.userprofile, name='userprofile'),
    path('doctorprofile/', views.doctorprofile, name='doctorprofile'),
    path('driverprofile/', views.driverprofile, name='driverprofile'),
    path('user_update/', views.user_update, name='user_update'),
    path('user_password/', views.user_password, name='user_password'),
    path('doctor_update/', views.doctor_update, name='doctor_update'),
    path('driver_update/', views.driver_update, name='driver_update'),
    path('doctor_password/', views.doctor_password, name='doctor_password'),
    path('driver_password/', views.driver_password, name='driver_password'),
    path('user_comment/', views.usercomment, name="usercomment"),
    path('user_comment_delete/<int:id>/', views.comment_delete, name="comment_delete")


]
