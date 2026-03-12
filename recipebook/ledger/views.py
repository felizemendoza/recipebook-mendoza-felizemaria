from django.shortcuts import render, redirect
from .models import Recipe, RecipeImage
from .forms import RecipeForm, RecipeImageForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipe_list.html"


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipe.html"
    form_class = RecipeForm
    redirect_field_name = "registration/login"

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = "recipe_add.html"
    form_class = RecipeForm
    redirect_field_name = "registration/login"

class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    template_name = "recipe_add_image.html"
    form_class = RecipeImageForm
    redirect_field_name = "registration/login"

    def get_success_url(self):
        return reverse_lazy('ledger:recipe_detail', kwargs={ 'pk': self.kwargs['pk'] })
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = RecipeImageForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.recipe_id = self.kwargs['pk']
            form.save()
            return redirect(self.get_success_url())
