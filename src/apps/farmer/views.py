from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import (
    FarmerCreateSerializer,
    FarmerSerializer
)
from .models import (
    FarmerModel
)


class FarmerViewSet(ModelViewSet):
    serializer_class = FarmerSerializer
    queryset = FarmerModel.objects.all()
    http_method_names = ["options", "get", "post", "patch", "put", "delete"]

    def create(self, request, *args, **kwargs):
        self.serializer_class = FarmerCreateSerializer
        return super().create(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):

        try:
            farmar_id = request.data.get("id")
            if not farmar_id:
                return self._bad_request("ID do agricultor é obrigatório.")
            
            farmer = get_object_or_404(FarmerModel, id=farmar_id)
            farmer.deleted = True
            farmer.save()

            serializer = FarmerSerializer(farmer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    @staticmethod
    def _bad_request(message):
        return Response({"error": message}, status=status.HTTP_400_BAD_REQUEST)
