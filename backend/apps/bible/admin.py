from django.contrib import admin
from apps.bible.models import Dictionary


@admin.register(Dictionary)
class DictionaryAdmin(admin.ModelAdmin):
    pass