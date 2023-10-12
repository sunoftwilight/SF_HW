from django.contrib import admin
from django.urls import path
from . import views

app_name = 'libraries'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:book_pk>/delete/<int:review_pk>/', views.delete, name='delete'),
]