from rest_framework import routers
from projects.views import (
    ProfileViewSet,
    ProjectViewSet,
    CertifyingInstitutionViewSet,
    CertificateViewSet,
)
from django.urls import path, include

router = routers.DefaultRouter()

router.register("profiles", ProfileViewSet)
router.register("projects", ProjectViewSet)
router.register("certifying-institutions", CertifyingInstitutionViewSet)
router.register("certificates", CertificateViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
