from django.urls import include, path
from rest_framework import routers
from .views import (
    FarmerViewSet
)

router = routers.DefaultRouter()
router.register(r"farmer", FarmerViewSet, basename="farmer")

urlpatterns = [
    path("", include(router.urls)),
]