from rest_framework import serializers
from .models import Versicle, Book, Version, Dictionary

class VersionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Version
        fields = "__all__"

class VersicleSerializer(serializers.ModelSerializer):

    version = serializers.SerializerMethodField()
    book = serializers.SerializerMethodField()

    class Meta:
        model = Versicle
        fields = "__all__"

    def get_version(self, obj):
        return VersionSerializer(obj.version).data

    def get_book(self, obj):
        return BooksSerializer(obj.book).data

class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"

class DictionarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Dictionary
        fields = "__all__"