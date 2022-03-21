from nturl2path import url2pathname
from django.urls import path 
from . import views 

urlpatterns = [
    # post views
    path('login/', views.user_login, name='login'), 
]
