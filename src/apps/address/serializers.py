from rest_framework import serializers
from .models import (
    AddressFarmerModel,
    AddressFarmModel
)


class AddressFarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressFarmerModel
        fields = "__all__"


class AddressFarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressFarmModel
        fields = "__all__"