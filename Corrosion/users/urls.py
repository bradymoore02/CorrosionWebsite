from django.urls import path
import os
from django.conf import settings
from users import views as user_views

urlpatterns = [
    path('register/', user_views.register, name='register'),
    ]
