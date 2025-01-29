from django.core.exceptions import ValidationError


def validation_total_area(total_area, agricultural_area, vegetation_area):
    if (agricultural_area + vegetation_area) > total_area:
        raise ValidationError("As áreas de agricultura e vegetação somadas, ultrapassam a área total.")
    