from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum
from django_filters import rest_framework as filters
from .serializers import (
    FarmSerializer
)
from .models import (
    FarmModel
)
from .filters import (
    FarmFilter
)


class FarmViewSet(ModelViewSet):
    serializer_class = FarmSerializer
    queryset = FarmModel.objects.all()
    http_method_names = ["options", "get", "post", "patch", "put"]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = FarmFilter


    @action(detail=False, methods=["GET"], name="quantity_all_farms")
    def quantity_all_farms(self, request, *args, **kwargs):
        quantity_farms = FarmModel.objects.count()

        return Response(data=quantity_farms, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=["GET"], name="quantity_all_total_area_farms")
    def quantity_all_total_area_farms(self, request, *args, **kwargs):
        quantity_total_area_farm = FarmModel.objects.aggregate(Sum('total_area_farm'))['total_area_farm__sum'] or 0
        
        return Response(data=quantity_total_area_farm, status=status.HTTP_200_OK)
