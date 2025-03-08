from urllib.parse import unquote

from django.db.models import F
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as rf_filters
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from apps.integration.api.serializers import MainPageSerializer, ContactPageSerializer, EstimationPageSerializer, \
    FranchisesSerializer, ArticleSerializer, BlogPageSerializer, PoliticsPageSerializer, CookiesPageSerializer, \
    MentionPageSerializer
from apps.integration.models import MainPage, ContactPage, EstimationPage, Franchises, Article, BlogPage, PoliticsPage, \
    MentionPage, CookiesPage


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


# class BlogViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = BlogPage.objects.all()
#     serializer_class = BlogPageSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#
#     def list(self, request, *args, **kwargs):
#         instance = BlogPage.objects.all().order_by('-id').first()
#         if not instance:
#             return Response({'detail': 'Not found.'}, status=404)
#
#         serializer = BlogPageSerializer(instance)
#         return Response(serializer.data)

class ArticlePagination(PageNumberPagination):
    page_size = 9
    page_size_query_param = 'page_size'
    max_page_size = 20


class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogPage.objects.all()
    serializer_class = BlogPageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        instance = BlogPage.objects.order_by('-id').first()
        if not instance:
            return Response({'detail': 'Not found.'}, status=404)

        # articles = instance.articles.all().order_by('-pub_date')

        # paginator = ArticlePagination()
        # paginated_articles = paginator.paginate_queryset(articles, request)

        blog_serializer = BlogPageSerializer(instance)
        # article_serializer = ArticleSerializer(paginated_articles, many=True)

        response_data = blog_serializer.data
        # response_data.update({'articles': paginator.get_paginated_response(article_serializer.data).data})

        return Response(response_data)


# class ArticleFilter(rf_filters.FilterSet):
#     tags__name = rf_filters.BaseInFilter(field_name='tags__name', lookup_expr='in')
#     # decoded_url = unquote(url)
#     class Meta:
#         model = Article
#         fields = ['tags__name']

class ArticleFilter(rf_filters.FilterSet):
    tags__name = rf_filters.BaseInFilter(field_name='tags__name', lookup_expr='in')

    def filter_tags_name(self, queryset, name, value):
        decoded_values = [unquote(v) for v in value]
        return queryset.filter(tags__name__in=decoded_values)

    class Meta:
        model = Article
        fields = ['tags__name']


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = ArticlePagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = ArticleFilter

    search_fields = ['title', 'description', 'author']

    def get_queryset(self):
        blog_page = BlogPage.objects.order_by('-id').first()
        if not blog_page:
            return Response({'detail': 'Not found.'}, status=404)

        queryset = blog_page.articles.all()

        # Получаем параметр сортировки из запроса
        sort_param = self.request.query_params.get('sort', 'date')

        if sort_param == 'reading_time':
            queryset = queryset.order_by(F('read_time').asc(nulls_last=True))  # NULL-значения в конце
        else:
            queryset = queryset.order_by(F('pub_date').desc(nulls_last=True))  # По умолчанию сортировка по дате

        return queryset


class PoliticsViewSet(viewsets.ModelViewSet):
    queryset = PoliticsPage.objects.all()
    serializer_class = PoliticsPageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        instance = PoliticsPage.objects.all().order_by('-id').first()
        if not instance:
            return Response({'detail': 'Not found.'}, status=404)

        serializer = PoliticsPageSerializer(instance)
        return Response(serializer.data)


class CookiesViewSet(viewsets.ModelViewSet):
    queryset = CookiesPage.objects.all()
    serializer_class = CookiesPageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        instance = CookiesPage.objects.all().order_by('-id').first()
        if not instance:
            return Response({'detail': 'Not found.'}, status=404)

        serializer = CookiesPageSerializer(instance)
        return Response(serializer.data)


class MentionViewSet(viewsets.ModelViewSet):
    queryset = MentionPage.objects.all()
    serializer_class = MentionPageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        instance = MentionPage.objects.all().order_by('-id').first()
        if not instance:
            return Response({'detail': 'Not found.'}, status=404)

        serializer = MentionPageSerializer(instance)
        return Response(serializer.data)
