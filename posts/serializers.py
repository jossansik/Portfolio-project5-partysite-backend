from rest_framework import serializers
from posts.models import Post
from likes.models import Like
from bookmarks.models import Bookmark
from tags.serializers import TagSerializer


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    bookmark_id = serializers.SerializerMethodField()
    bookmarks_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    post_tags = TagSerializer(many=True, read_only=True)

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    def get_bookmark_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            bookmark = Bookmark.objects.filter(
                owner=user, post=obj
            ).first()
            return bookmark.id if bookmark else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'is_owner', 'owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'category',
            'like_id', 'likes_count',
            'comments_count', 'bookmark_id', 'bookmarks_count', 'post_tags',
        ]
        extra_kwargs = {'post_tags': {'required': False}}
