from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'', UserViewSet, basename='users')

urlpatterns = [
    # /api/users/...
] + router.urls

