from rest_framework import viewsets, status
from django.utils.translation import ugettext_lazy as _
from rest_framework import viewsets, status
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from library.utils import SimplePaginator
from django.conf import settings
from .serializers import VersiculosSerializer, BooksSerializer, VersoesSerializer, DicionarioSerializer
from .models import Versiculos, Livros, Versoes, Dicionario
import requests
import json
from .filters import LivrosFilter, VersiculoFilter
from django.db.models import Count

class BibliaViewSet(viewsets.GenericViewSet, SimplePaginator):

    serializer_class = VersiculosSerializer
    permission_classes = [ AllowAny ]
    parser_classes = ( MultiPartParser, FormParser, JSONParser)

    # last inserted in DB (For home products)
    @action(methods=['get'], detail=False, permission_classes=[AllowAny])
    def books(self, request):
        books = LivrosFilter(request.GET, queryset=Livros.objects.all())

        return Response(BooksSerializer(books.qs, many=True).data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, permission_classes=[AllowAny])
    def versiculos(self, request):
        vers = VersiculoFilter(request.GET, queryset=Versiculos.objects.all())

        return self.serializer_paginator(vers.qs, VersiculosSerializer)

    @action(methods=['get'], detail=False, permission_classes=[AllowAny])
    def capitulos_livro(self, request):
        
        versao = request.GET.get("versao_id", 1)
        livro = request.GET.get("livro_id", 1)

        capitulos = Versiculos.objects.values("ver_capitulo").filter(ver_liv_id=livro, ver_vrs_id=versao).distinct()

        return Response(capitulos, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, permission_classes=[AllowAny])
    def get_versoes(self, request):

        qry = Versoes.objects.all()

        response = VersoesSerializer(qry, many=True).data

        return Response(response, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False, permission_classes=[AllowAny])
    def get_dicionario(self, request):
        dics = request.data
        qry = Dicionario.objects.filter(id__in=dics)
        response = DicionarioSerializer(qry, many=True).data

        return Response(response, status=status.HTTP_200_OK)