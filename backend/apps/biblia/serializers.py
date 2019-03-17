from rest_framework import serializers
from .models import Versiculos, Livros

class VersiculosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Versiculos
        fields = "__all__"

class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Livros
        fields = "__all__"