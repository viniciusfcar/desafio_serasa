from rest_framework import serializers
from .models import (
    FarmerModel
)


class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmerModel
        fields = "__all__"


class FarmerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmerModel
        fields = [
            "name",
            "document",
            "address",
        ]
