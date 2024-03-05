from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView,CreateView,DeleteView,UpdateView
from .models import Cheese

import logging

log = logging.getLogger(__name__)


class CheeseListView(ListView):
    model = Cheese
    def get_context_data (self,**kwargs):
        context = super().get_context_data(**kwargs)
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

class CheeseUpdateView(UpdateView):
    model = Cheese
    fields = [
        'name',
        'description',
        'firmness',
        'country_of_origin',
    ]
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse_lazy('cheeses:detail', args=[self.object.slug])