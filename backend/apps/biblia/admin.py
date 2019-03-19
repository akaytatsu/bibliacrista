from django.contrib import admin
from apps.biblia.models import Dicionario


@admin.register(Dicionario)
class DicionarioAdmin(admin.ModelAdmin):
    pass