from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from apps.integration.api.serializers import MainPageSerializer
from apps.integration.models import MainPage


class MainPageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MainPage.objects.all()
    serializer_class = MainPageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        instance = MainPage.objects.all().order_by('-id').first()
        if not instance:
            return Response({'detail': 'Not found.'}, status=404)

        serializer = MainPageSerializer(instance)
        return Response(serializer.data)
