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
from .serializers import VersicleSerializer, BooksSerializer, VersicleSerializer, DictionarySerializer, VersionSerializer
from .models import Versicle, Book, Version, Dictionary
import requests
import json
from .filters import BookFilter, VersicleFilter
from django.db.models import Count

class BibleViewSet(viewsets.GenericViewSet, SimplePaginator):

    serializer_class = VersicleSerializer
    permission_classes = [ AllowAny ]
    parser_classes = ( MultiPartParser, FormParser, JSONParser)

    # last inserted in DB (For home products)
    @action(methods=['get'], detail=False, permission_classes=[AllowAny])
    def books(self, request):
        books = BookFilter(request.GET, queryset=Book.objects.all())

        return Response(BooksSerializer(books.qs, many=True).data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, permission_classes=[AllowAny])
    def versicles(self, request):
        vers = VersicleFilter(request.GET, queryset=Versicle.objects.all())

        print("*********")
        print(vers.qs.query)
        return self.serializer_paginator(vers.qs, VersicleSerializer)

    @action(methods=['get'], detail=False, permission_classes=[AllowAny])
    def book_chapters(self, request):
        
        version_id = request.GET.get("version_id", 1)
        book_id = request.GET.get("book_id", 1)

        chapters = Versicle.objects.values("chapter").filter(book_id=book_id, version_id=version_id).distinct()

        return Response(chapters, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, permission_classes=[AllowAny])
    def get_versions(self, request):

        qry = Version.objects.all()

        response = VersionSerializer(qry, many=True).data

        return Response(response, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False, permission_classes=[AllowAny])
    def get_dictionary(self, request):
        dics = request.data
        qry = Dictionary.objects.filter(id__in=dics)
        response = DictionarySerializer(qry, many=True).data

        return Response(response, status=status.HTTP_200_OK)