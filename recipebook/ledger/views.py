from django.shortcuts import render
from .models import Recipe
from .forms import RecipeForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


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

    # def form_valid(self, form):
    #     form.instance.created_by = self.request.user
    #     return super().form_valid(form)
