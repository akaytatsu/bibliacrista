import hashlib
import random
import string
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.response import Response
from rest_framework import permissions
from django.conf import settings


class SimplePaginator():
    def serializer_paginator(self, queryset, serializer_instance):

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = serializer_instance(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = serializer_instance(queryset, many=True)

        return Response(serializer.data)