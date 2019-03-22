import hashlib
import random
import string
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.response import Response
from rest_framework import permissions
from django.conf import settings
from django.utils.functional import cached_property

class SimplePaginator():
    def serializer_paginator(self, queryset, serializer_instance):

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = serializer_instance(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = serializer_instance(queryset, many=True)

        return Response(serializer.data)

class CustomResultsSetPagination(PageNumberPagination):
    page_size = 20

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'pages': self.page.paginator.num_pages,
            'page_size': self.page_size,
            'results': data
        })