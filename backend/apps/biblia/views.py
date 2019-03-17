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
from .serializers import VersiculosSerializer, BooksSerializer
from .models import Versiculos, Livros
import requests
import json


class BibliaViewSet(viewsets.GenericViewSet, SimplePaginator):

    serializer_class = VersiculosSerializer
    permission_classes = [ AllowAny ]
    parser_classes = ( MultiPartParser, FormParser, JSONParser)

    # last inserted in DB (For home products)
    @action(methods=['get'], detail=False, permission_classes=[AllowAny])
    def books(self, request):
        books = Livros.objects.all()
        return Response(BooksSerializer(books, many=True).data, status=status.HTTP_200_OK)