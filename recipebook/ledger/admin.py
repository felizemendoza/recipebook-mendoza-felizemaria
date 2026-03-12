from django.contrib import admin
from .models import Recipe, RecipeIngredient, Profile, RecipeImage
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = [
        ProfileInline,
    ]


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeImageInline(admin.TabularInline):
    model = RecipeImage

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [
        RecipeIngredientInline, RecipeImageInline
    ]



admin.site.register(Recipe, RecipeAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
