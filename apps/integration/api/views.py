from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from apps.integration.api.serializers import MainPageSerializer, ContactPageSerializer, EstimationPageSerializer, \
    FranchisesSerializer, ArticleSerializer, BlogPageSerializer
from apps.integration.models import MainPage, ContactPage, EstimationPage, Franchises, Article, BlogPage


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


# ViewSets
class ContactPageViewSet(viewsets.ModelViewSet):
    queryset = ContactPage.objects.all()
    serializer_class = ContactPageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        instance = ContactPage.objects.all().order_by('-id').first()
        if not instance:
            return Response({'detail': 'Not found.'}, status=404)

        serializer = ContactPageSerializer(instance)
        return Response(serializer.data)


class EstimationPageViewSet(viewsets.ModelViewSet):
    queryset = EstimationPage.objects.all()
    serializer_class = EstimationPageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        instance = EstimationPage.objects.all().order_by('-id').first()
        if not instance:
            return Response({'detail': 'Not found.'}, status=404)

        serializer = EstimationPageSerializer(instance)
        return Response(serializer.data)


class FranchisesViewSet(viewsets.ModelViewSet):
    queryset = Franchises.objects.all()
    serializer_class = FranchisesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        instance = Franchises.objects.all().order_by('-id').first()
        if not instance:
            return Response({'detail': 'Not found.'}, status=404)

        serializer = FranchisesSerializer(instance)
        return Response(serializer.data)


class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogPage.objects.all()
    serializer_class = BlogPageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        instance = BlogPage.objects.all().order_by('-id').first()
        if not instance:
            return Response({'detail': 'Not found.'}, status=404)

        serializer = BlogPageSerializer(instance)
        return Response(serializer.data)


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all().order_by('-pub_date')
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    filterset_fields = ['tags__name']

    search_fields = ['title', 'description', 'author']

