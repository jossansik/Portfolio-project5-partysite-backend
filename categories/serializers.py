from rest_framework import serializers
from categories.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id', 'name',
            'image', 'created_at', 'updated_at'
        ]


class CategoryDetailSerializer(CategorySerializer):
    class Meta:
        model = Category
        fields = [
            'id', 'name',
            'image', 'created_at', 'updated_at'
        ]
