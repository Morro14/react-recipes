from django.contrib import admin

# Register your models here.

from .models import Recipe, Category


class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category)
