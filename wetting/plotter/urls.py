from django.urls import path
import os
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.home, name='plotter-home'),
    path('drops/', views.DropListView.as_view(), name='plotter-drops'),
    path('drop/<int:pk>',
         views.DropDetailView.as_view(),
         name='plotter-drop-detail'),
    path('tests/', views.TestListView.as_view(), name='plotter-tests'),
]
