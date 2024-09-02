from rest_framework import serializers
from .models import FoodRecipe

class FoodRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodRecipe
        fields = '__all__'

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name cannot be blank.")
        if FoodRecipe.objects.filter(name=value).exists():
            raise serializers.ValidationError("A recipe with this name already exists.")
        return value

    def validate_description(self, value):
        if not value.strip():
            raise serializers.ValidationError("Description cannot be blank.")
        return value

    def validate_ingredients(self, value):
        if not value.strip():
            raise serializers.ValidationError("Ingredients cannot be blank.")
        return value

    def validate_method(self, value):
        if not value.strip():
            raise serializers.ValidationError("Method cannot be blank.")
        return value

    def validate_category(self, value):
        if not value.strip():
            raise serializers.ValidationError("Category cannot be blank.")
        return value
    
# Validated successfully