from rest_framework import routers
from projects.views import ProfileViewSet
from django.urls import path, include

router = routers.DefaultRouter()

router.register("", ProfileViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
