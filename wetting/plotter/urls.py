from django.urls import path
import os
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.home, name='corrosion-home'),
    path('techniques/', views.DropListView.as_view(), name='techniques'),
    path('drop/<int:pk>',
         views.DropDetailView.as_view(),
         name='plotter-drop-detail'),
    path('tests/', views.TestListView.as_view(), name='plotter-tests'),
]
