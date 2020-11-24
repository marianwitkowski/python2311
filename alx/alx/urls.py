from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="ALX Test API",
        default_version="v1",
        description="Opis API",
        terms_of_service="http://alx.pl",
        contact=openapi.Contact(email="jan@kowalski.pl"),
        license=openapi.License(name="MIT License")
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)


urlpatterns = [

    url(r"^swagger(?P<format>\.json|\.yaml)", schema_view.without_ui() ),
    url(r"^swagger/$", schema_view.with_ui('swagger'), name='schema-swagger-ui'  ),
    url(r"^redoc/$", schema_view.with_ui('redoc')),

    path('api/', include("rentflat.urls")  ),
    path('admin/', admin.site.urls),
    path("", include("movies.urls") )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
