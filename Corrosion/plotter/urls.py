from django.urls import path
import os
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.home, name='corrosion-home'),
    path('techniques/', views.TechniqueListView.as_view(), name='techniques'),
    path('technique/<int:pk>', views.TechniqueDetailView.as_view(), name='technique-detail'),
    path('materials/', views.MaterialListView.as_view(), name='materials'),
    path('materials/<int:pk>', views.MaterialDetailView.as_view(), name='material-detail'),
    path('materials/sample/<int:pk>', views.SampleDetailView.as_view(), name='sample-detail')
         ]
