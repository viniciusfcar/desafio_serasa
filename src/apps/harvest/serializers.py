from rest_framework import serializers
from .models import (
    HarvestModel
)


class HarvestSerializer(serializers.ModelSerializer):
    class Meta:
        model = HarvestModel
        fields = "__all__"