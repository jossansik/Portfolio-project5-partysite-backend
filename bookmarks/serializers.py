from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from posts.serializers import PostSerializer
from .models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    post_entity = PostSerializer(source='post', read_only=True)

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    class Meta:
        model = Bookmark
        fields = [
            'id', 'owner', 'profile_id', 'profile_image',
            'post', 'created_at', 'post_entity'
        ]
