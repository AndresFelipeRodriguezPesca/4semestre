from django.contrib import admin
from django.urls import path
from . import views

app_name = "characters"

urlpatterns = [
    path('',views.list, name='list_characters'),
    path('save', views.save, name='save_characters'),
    path('edit/<int:id>',views.edit, name='edit'),
    path('detail/<int:id>', views.detail, name='detail_characters'),
    path('punto_uno',views.puntoUno),

]
