from projects.models import Profile
from projects.serializers import ProfileSerializer
from rest_framework import viewsets, permissions


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
