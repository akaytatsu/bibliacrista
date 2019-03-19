from rest_framework import serializers
from .models import Versiculos, Livros, Versoes, Dicionario

class VersoesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Versoes
        fields = "__all__"

class VersiculosSerializer(serializers.ModelSerializer):

    ver_vrs = serializers.SerializerMethodField()
    ver_liv = serializers.SerializerMethodField()

    class Meta:
        model = Versiculos
        fields = "__all__"

    def get_ver_vrs(self, obj):
        return VersoesSerializer(obj.ver_vrs).data

    def get_ver_liv(self, obj):
        return BooksSerializer(obj.ver_liv).data

class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Livros
        fields = "__all__"

class DicionarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dicionario
        fields = "__all__"