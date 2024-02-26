from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView,CreateView,DeleteView
from .models import Cheese

import logging

log = logging.getLogger(__name__)


class CheeseListView(ListView):
    model = Cheese

    def get_context_data (self,**kwargs):
        log.info("Hello World")
        context = super().get_context_data(**kwargs)
        # context['cheese_list'] = Cheese.objects.all()
        return context

class CheeseDetailView(DetailView):
    model = Cheese

class CheeseCreateView(CreateView):
    model = Cheese
    
    fields = [
        'name',
        'description',
        'firmness',
        'country_of_origin',
    ]

class CheeseDeleteView(DeleteView):
    model = Cheese
    templare_name = '../templates/cheeses/cheese_confirm_delete.html'
    success_url = reverse_lazy("cheeses:list")

 