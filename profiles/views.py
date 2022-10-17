from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from startsite.permissions import IsOwnerOrReadOnly
from .serializers import ProfileSerializer
from .models import Profile


class ProfileList(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate().order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate().order_by('-created_at')
    serializer_class = ProfileSerializer
