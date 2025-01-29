from rest_framework.viewsets import ModelViewSet
from .serializers import (
    AddressFarmerSerializer,
    AddressFarmSerializer
)
from .models import (
    AddressFarmerModel,
    AddressFarmModel
)


class AddressFarmerViewSet(ModelViewSet):
    serializer_class = AddressFarmerSerializer
    queryset = AddressFarmerModel.objects.all()
    http_method_names = ["options", "get", "post", "patch", "put"]


class AddressFarmViewSet(ModelViewSet):
    serializer_class = AddressFarmSerializer
    queryset = AddressFarmModel.objects.all()
    http_method_names = ["options", "get", "post", "patch", "put"]
