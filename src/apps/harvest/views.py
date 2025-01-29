from rest_framework.viewsets import ModelViewSet
from .serializers import (
    HarvestSerializer
)
from .models import (
    HarvestModel
)


class HarvestViewSet(ModelViewSet):
    serializer_class = HarvestSerializer
    queryset = HarvestModel.objects.all()
    http_method_names = ["options", "get", "post", "patch", "put"]
