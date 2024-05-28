from rest_framework import routers
from projects.views import ProfileViewSet, ProjectViewSet
from django.urls import path, include

router = routers.DefaultRouter()

router.register("profiles", ProfileViewSet)
router.register("projects", ProjectViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
