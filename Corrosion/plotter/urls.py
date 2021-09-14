from django.urls import path
import os
from django.conf import settings
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.home, name='corrosion-home'),
    path('techniques/', login_required(views.TechniqueListView.as_view()), name='techniques'),
    path('technique/<int:pk>', login_required(views.TechniqueDetailView.as_view()), name='technique-detail'),
    path('materials/', login_required(views.MaterialListView.as_view()), name='materials'),
    path('materials/<int:pk>', login_required(views.MaterialDetailView.as_view()), name='material-detail'),
    path('materials/sample/<int:pk>', login_required(views.SampleDetailView.as_view()), name='sample-detail'),

         ]
