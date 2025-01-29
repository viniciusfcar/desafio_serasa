from rest_framework import serializers
from .models import (
    FarmModel
)


class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmModel
        fields = "__all__"