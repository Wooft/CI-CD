from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title', 'description'] #Атрибуты по которым происходит фильтрация
    search_fields = ['title', 'description']#Атрибуты для фильтра, который осуществляет поиск по тексту
    pagination_class = LimitOffsetPagination

    @action(['GET'], detail=False)
    def test(self, request):
        return Response('Deploy вечен')

    @action(['GET'], detail=False)
    def test2(self, request):
        return Response('Тест прошел успешно')

    @action(['GET'], detail=False)
    def test3(self, request):
        return Response('Привет, Олечка')



class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['products', ]
    search_fields = ['address', ]

