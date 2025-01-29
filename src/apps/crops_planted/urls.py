from django.urls import include, path
from rest_framework import routers
from .views import (
    CropsPlantedViewSet
)

router = routers.DefaultRouter()
router.register(r"crops_planted", CropsPlantedViewSet, basename="crops_planted")

urlpatterns = [
    path("", include(router.urls)),
]