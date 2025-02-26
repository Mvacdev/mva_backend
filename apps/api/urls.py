
from django.urls import path, include


urlpatterns = [
    # /api/...
    path('', include('apps.core.api.urls')),
    path('users/', include('apps.users.api.urls')),
    path('integration/', include('apps.integration.api.urls')),

    # path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', CookieTokenRefreshView.as_view(), name='token_refresh'),

    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/', CookieTokenObtainPairView.as_view(), name='token_obtain_pair'),
]


