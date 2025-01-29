from rest_framework.viewsets import ModelViewSet
from .serializers import (
    CropsPlantedSerializer
)
from .models import (
    CropsPlantedModel
)


class CropsPlantedViewSet(ModelViewSet):
    serializer_class = CropsPlantedSerializer
    queryset = CropsPlantedModel.objects.all()
    http_method_names = ["options", "get", "post", "patch", "put"]
