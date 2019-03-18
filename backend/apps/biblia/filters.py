import django_filters
from .models import Versiculos, Livros
from django_filters import rest_framework as filters


class VersiculoFilter(django_filters.FilterSet):

    livro_id = django_filters.NumberFilter(field_name="ver_liv_id", )
    livro_nome = django_filters.NumberFilter(field_name="ver_liv__liv_nome", )
    versao_id = django_filters.NumberFilter(field_name="ver_vrs_id", )
    versao_nome = django_filters.CharFilter(field_name="ver_vrs__vrs_nome", )
    capitulo = django_filters.NumberFilter(field_name="ver_capitulo", )
    versiculo = django_filters.NumberFilter(field_name="ver_versiculo", )
    texto = django_filters.CharFilter(field_name="ver_texto", lookup_expr="icontains")

    class Meta:
        model = Versiculos
        fields = ['ver_id', ]

class LivrosFilter(django_filters.FilterSet):

    id = django_filters.NumberFilter(field_name="liv_id", )
    testamento = django_filters.NumberFilter(field_name="liv_tes__tes_nome", )
    nome = django_filters.CharFilter(field_name="liv_nome", lookup_expr="icontains")

    class Meta:
        model = Livros
        fields = ('id', 'testamento', 'nome', )