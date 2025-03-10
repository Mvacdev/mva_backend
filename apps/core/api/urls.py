from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.core.api.views import SearchCarsAPIView, DataHistoryAPIView, PotentialFranchiseAPIView

# Create a router and register our viewsets with it.
router = DefaultRouter()
# router.register(r'status', StatusViewSet, basename='status')


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('search_cars/', SearchCarsAPIView.as_view(), name='search_cars'),
    path('write_history/', DataHistoryAPIView.as_view(), name='write_history'),
    path('write_franchise/', PotentialFranchiseAPIView.as_view(), name='write_franchise'),
    # path('', index, name='index'),
    # path('alarm_mess/', index_1, name='index_1'),
] + router.urls
