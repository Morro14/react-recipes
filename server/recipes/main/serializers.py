from rest_framework import serializers
from .models import Recipe, Category


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    recipes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Category
        fields = ["name", "slug", "recipes"]

    def get_recipes(self, obj) -> list | dict:

        recipes = Recipe.objects.filter(category=obj.id)
        print("Recipes", recipes)
        recipes = RecipeSerializer(recipes, many=True)
        return recipes.data
