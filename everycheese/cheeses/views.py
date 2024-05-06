from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .forms import CheeseUpdateForm, RatingForm
from .models import Cheese, Rating
from django.shortcuts import render


class CheeseListView(ListView):
    model = Cheese

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.prefetch_related('ratings') 
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Calculate average rating for each cheese
        for cheese in context['object_list']:
            cheese.average_rating = cheese.calculate_average_rating()
        return context


class CheeseDetailView(DetailView):
    model = Cheese


class CheeseCreateView(CreateView):
    model = Cheese
    fields = ['name', 'description', 'firmness', 'country_of_origin']


class CheeseDeleteView(DeleteView):
    model = Cheese
    success_url = reverse_lazy('cheeses:list')


class CheeseUpdateView(UpdateView):
    model = Cheese
    form_class = CheeseUpdateForm
    template_name = "cheeses/cheese_update.html"  
    success_url = reverse_lazy('cheeses:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'rating_form' not in context:
            context['rating_form'] = RatingForm()
        return context
    
    def form_valid(self, form):
        rating_form = RatingForm(self.request.POST)
        if rating_form.is_valid():
            self.object = form.save()
            rating = rating_form.save(commit=False)
            rating.cheese = self.object
            rating.save()
            return super().form_valid(form)
        else:
            return render(self.request, self.template_name, self.get_context_data(form=form, rating_form=rating_form))
