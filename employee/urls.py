from django.contrib import admin
from django.urls import path
from employee import views

urlpatterns = [
    path('',views.home,name='home'),
    path('showinfo/',views.showinfo,name='showinfo'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('<int:id>/',views.update,name='update'),
     
]
