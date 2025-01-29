from django.urls import include, path
from rest_framework import routers
from .views import (
    FarmViewSet
)

router = routers.DefaultRouter()
router.register(r"farm", FarmViewSet, basename="farm")

urlpatterns = [
    path("", include(router.urls)),
]