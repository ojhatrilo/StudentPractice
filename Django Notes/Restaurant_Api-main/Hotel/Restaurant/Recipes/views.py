from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import FoodRecipe
from .serializers import FoodRecipeSerializer

@api_view(['GET'])
def food_recipe_list(request):
    category = request.query_params.get('category', None)
    if category:
        recipes = FoodRecipe.objects.filter(category=category)
    else:
        recipes = FoodRecipe.objects.all()
    serializer = FoodRecipeSerializer(recipes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def food_recipe_create(request):
    serializer = FoodRecipeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def food_recipe_update(request, pk):
    try:
        recipe = FoodRecipe.objects.get(pk=pk)
    except FoodRecipe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = FoodRecipeSerializer(recipe, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)