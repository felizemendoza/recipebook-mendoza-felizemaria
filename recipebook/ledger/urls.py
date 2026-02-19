from django.urls import path
from .views import recipes, recipe1, recipe2, RecipeListView, RecipeDetailView

urlpatterns = [
    # path('recipes/list', recipes, name = 'recipes'),
    # path('recipe/1', recipe1, name = 'recipe 1'),
    # path('recipe/2', recipe2, name = 'recipe 2'),
    path('recipes/list', RecipeListView.as_view(), name='recipe_list'),
    path('<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
]

app_name = "ledger"