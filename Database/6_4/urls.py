# accounts/urls.py

from django.urls import path
from . import views 


app_name = 'accounts'
urlpatterns = [
    ...
    path('<int:__(a)__>/follow/', views.follow, name='follow'),
]


# (a) : user_pk