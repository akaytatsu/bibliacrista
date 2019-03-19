from django.core.management.base import BaseCommand, CommandError
from apps.bible.models import Dictionary, Versicle

class Command(BaseCommand):
    help = 'Sincroniza dicionario na base de dados'

    def handle(self, *args, **options):
        
        dictionaries = Dictionary.objects.all()

        for dic in dictionaries:
            versicles = Versicle.objects.filter(ver_texto__icontains=dic.term).all()

            for ver in verversiclessiculos:
                ver.dictionary.add(dic)
