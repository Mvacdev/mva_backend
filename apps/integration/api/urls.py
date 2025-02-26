from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.integration.api.views import MainPageViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'main-page', MainPageViewSet, basename='main-page')

urlpatterns = router.urls
