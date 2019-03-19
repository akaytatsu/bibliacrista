import django_filters
from .models import Versicle, Book
from django_filters import rest_framework as filters


class VersicleFilter(django_filters.FilterSet):

    book_id = django_filters.NumberFilter(field_name="book_id", )
    book_name = django_filters.NumberFilter(field_name="book__name", )
    version_id = django_filters.NumberFilter(field_name="version_id", )
    version_name = django_filters.CharFilter(field_name="version__name", )
    chapter = django_filters.NumberFilter(field_name="chapter", )
    versicle = django_filters.NumberFilter(field_name="versicle", )
    text = django_filters.CharFilter(field_name="text", lookup_expr="icontains")

    class Meta:
        model = Versicle
        fields = ['id', ]

class BookFilter(django_filters.FilterSet):

    id = django_filters.NumberFilter(field_name="id", )
    testament = django_filters.NumberFilter(field_name="testament__name", )
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Book
        fields = ('id', )