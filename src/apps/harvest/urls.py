from django.urls import include, path
from rest_framework import routers
from .views import (
    HarvestViewSet
)

router = routers.DefaultRouter()
router.register(r"harvest", HarvestViewSet, basename="harvest")

urlpatterns = [
    path("", include(router.urls)),
]