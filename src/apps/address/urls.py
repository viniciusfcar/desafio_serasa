from django.urls import include, path
from rest_framework import routers
from .views import (
    AddressFarmerViewSet,
    AddressFarmViewSet
)

router = routers.DefaultRouter()
router.register(r"address_farmer", AddressFarmerViewSet, basename="address_farmer")
router.register(r"address_farm", AddressFarmViewSet, basename="address_farm")

urlpatterns = [
    path("", include(router.urls)),
]