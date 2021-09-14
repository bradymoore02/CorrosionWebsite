from django.shortcuts import render
from plotly.offline import plot
from plotter.models import Technique, Material, Sample
from .forms import MyForm
import plotly.express as px
from django.utils.datastructures import MultiValueDictKeyError
from django import forms
import pandas as pd
import numpy as np
from django.views import generic
import plotly.graph_objects as go
from django.shortcuts import redirect
import re

def home(request):
    """TODO: Docstring for home.

    :request: TODO
    :returns: TODO

    """

    return render(request, "plotter/home.html")

class TechniqueListView(generic.ListView):
    model = Technique

class TechniqueDetailView(generic.DetailView):
    model = Technique

class MaterialListView(generic.ListView):
    model = Material

class MaterialDetailView(generic.DetailView):
    model = Material

class SampleDetailView(generic.DetailView):
    model = Sample
