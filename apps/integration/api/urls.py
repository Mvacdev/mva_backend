from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.integration.api.views import MainPageViewSet, ContactPageViewSet, EstimationPageViewSet, FranchisesViewSet, \
    ArticleViewSet, BlogViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'main-page', MainPageViewSet, basename='main-page')
router.register(r'contact-page', ContactPageViewSet, basename='contact-page')
router.register(r'estimation-page', EstimationPageViewSet, basename='estimation-page')
router.register(r'franchises-page', FranchisesViewSet, basename='franchises-page')
router.register(r'blog-page', BlogViewSet, basename='blog-page')
router.register(r'articles', ArticleViewSet, basename='article')

urlpatterns = router.urls
