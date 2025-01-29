from rest_framework import serializers
from .models import CropsPlantedModel


class CropsPlantedSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropsPlantedModel
        fields = "__all__"