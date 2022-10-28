from rest_framework import generics, permissions, filters
from tags.serializers import TagSerializer, TagDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .models import Tag


class TagList(generics.ListCreateAPIView):
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Tag.objects.annotate(
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = ['category']


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TagDetailSerializer
    queryset = Tag.objects.all()
