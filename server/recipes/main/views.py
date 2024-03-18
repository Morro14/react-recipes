from django.shortcuts import render
from .models import Recipe, Category
from .serializers import RecipeSerializer, CategorySerializer
from rest_framework import viewsets, status, views
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view, action


# Create your views here.
class RecipeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for retrieving recipes.
    """

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    lookup_field = "slug"


recipe_detail = RecipeViewSet.as_view({"get": "retrieve"})
recipe_list = RecipeViewSet.as_view({"get": "list"})


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for retrieving Categories.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "slug"


category_details = CategoryViewSet.as_view({"get": "retrieve"})
category_list = CategoryViewSet.as_view({"get": "list"})


# @api_view(["GET"])
# def category_recipes(request, slug):
#     """A viewset for retrieving recipes in certain category"""
#     serializer_class = CategorySerializer
#     try:
#         category = Category.objects.get(slug=slug)
#     except Category.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":

#         recipes = Recipe.objects.filter(category=category)
#         serializer = RecipeSerializer(recipes, many=True)
#         return Response(serializer.data)
