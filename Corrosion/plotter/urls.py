from django.urls import path
import os
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.home, name='corrosion-home'),
    path('techniques/', views.TechniqueListView.as_view(), name='techniques'),
    path('technique/<int:pk>',
         views.TechniqueDetailView.as_view(),
         name='plotter-technique-detail')
         ]
