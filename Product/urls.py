from django.urls import path
from .import views
urlpatterns = [
    path('comment_Add/<int:id>/', views.Comment_Add,name ='comment_Add'),


]