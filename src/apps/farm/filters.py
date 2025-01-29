import django_filters
from .models import FarmModel


class FarmFilter(django_filters.FilterSet):
    state = django_filters.CharFilter(
        field_name="address__state", lookup_expr="exact"
    )

    crops_planted = django_filters.CharFilter(
        field_name="crops_planted_farm__id", lookup_expr="exact"
    )

    agricultural_area = django_filters.CharFilter(
        field_name="agricultural_area", lookup_expr="exact"
    )

    vegetation_area = django_filters.CharFilter(
        field_name="vegetation_area", lookup_expr="exact"
    )

    class Meta:
        model = FarmModel
        fields = [
            "state",
            "crops_planted",
            "agricultural_area",
            "vegetation_area",
        ]