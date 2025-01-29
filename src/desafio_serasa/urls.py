
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API Serasa",
        default_version='v1',
        description="API DESAFIO SERASA"
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("apps.farmer.urls")),
    path("api/", include("apps.address.urls")),
    path("api/", include("apps.crops_planted.urls")),
    path("api/", include("apps.farm.urls")),
    path("api/", include("apps.harvest.urls")),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
