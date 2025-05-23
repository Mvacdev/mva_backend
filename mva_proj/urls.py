"""
URL configuration for MVA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions

schema_view = get_schema_view(
   openapi.Info(
      title="API documentation",
      default_version='v1',
      description="",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email=""),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.api.urls')),
    path('auth/', include('drf_social_oauth2.urls', namespace='drf')),  # main authorization
    # Swagger
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('trix-editor/', include('trix_editor.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),

    # path('', include('apps.core.urls')),
    # path('users/', include('apps.users.urls')),
    # path('auth/', include('drf_social_oauth2.urls', namespace='drf'))
]

if not settings.IS_PRODUCTION_ENV:
    import debug_toolbar

    urlpatterns += [
        # Django Debug toolbar
        path('', include(router.urls)),
        path('__debug__/', include(debug_toolbar.urls)),
        path('api-auth/', include('rest_framework.urls'))


    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
