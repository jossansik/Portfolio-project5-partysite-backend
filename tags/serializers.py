from rest_framework import serializers
from tags.models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'id', 'name', 'created_at', 'updated_at',
            'category', 'posts'
        ]
        extra_kwargs = {'posts': {'required': False}}


class TagDetailSerializer(TagSerializer):
    category = serializers.ReadOnlyField(source='category.id')
