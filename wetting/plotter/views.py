from django.shortcuts import render
from plotly.offline import plot
from plotter.models import Drop, Substrate, Test
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
    substrates = Substrate.objects.all()
    options = [i.name for i in substrates]
    form = MyForm(request.POST or None, options=options)
    if request.method == "POST":
        df = pd.DataFrame()
        for option in options:
            try:
                if request.POST[option] == 'on':
                    data = Drop.objects.order_by('stage_temp').filter(
                        test__substrate__name=option)
                    tmp = pd.DataFrame.from_records(data.values())
                    tmp['substrate'] = [i.test.substrate.name for i in data]
                    tmp['date'] = [
                        i.test.date.strftime('%m/%d/%Y') for i in data
                    ]
                    try:
                        df = df.append(tmp)
                    except ValueError:
                        df = tmp
            except MultiValueDictKeyError:
                pass
        try:
            Plot = px.scatter(df,
                              x='stage_temp',
                              y='contact_angle',
                              color='substrate',
                              labels={
                                  'stage_temp': 'Stage Temperature',
                                  'contact_angle': 'Contact Angle',
                                  'tip_temp': 'Tip Temperature',
                                  'substrate': 'Substrate',
                                  'date': 'Date',
                              },
                              hover_data={
                                  'tip_temp': True,
                                  'date': True,
                                  'id': False,
                              },
                              range_y=[0, df['contact_angle'].max() + 5],
                              width=850)
            Plot.update_traces(marker=dict(size=12))
        except ValueError:
            pass
        except KeyError:
            pass
    try:
        Plot
    except NameError:
        Plot = px.line(
            x=[0.],
            y=[0.],
            width=850,
        )
    plot_div = plot(Plot,
                    output_type='div',
                    include_plotlyjs=False,
                    show_link=False,
                    link_text='')
    res = re.search('<div id="([^"]*)"', plot_div)
    div_id = res.groups()[0]

    # Build JavaScript callback for handling clicks
    # and opening the URL in the trace's customdata
    return render(request,
                  "plotter/home.html",
                  context={
                      'plot_div': plot_div,
                      'form': form,
                      'div_id': div_id,
                  })


class DropListView(generic.ListView):
    model = Drop


class DropDetailView(generic.DetailView):
    model = Drop

class TestListView(generic.ListView):
    model = Test
