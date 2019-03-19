from django.core.management.base import BaseCommand, CommandError
from apps.biblia.models import Dicionario, Versiculos

class Command(BaseCommand):
    help = 'Sincroniza dicionario na base de dados'

    def handle(self, *args, **options):
        
        dicionarios = Dicionario.objects.all()

        for dic in dicionarios:
            versiculos = Versiculos.objects.filter(ver_texto__icontains=dic.palavra).all()

            for ver in versiculos:
                ver.dicionario.add(dic)
