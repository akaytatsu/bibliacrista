from django.core.management.base import BaseCommand, CommandError
from apps.bible.models import Dictionary, Versicle, Version
from requests import request
from bs4 import BeautifulSoup
from tqdm import tqdm

class Command(BaseCommand):
    help = 'Sincroniza dicionario na base de dados'

    def contents_to_string(self, contents):
        aux = ""
        for aux2 in contents:
            aux = aux + "{}".format(aux2)

        return BeautifulSoup(aux, "lxml").text

    def handle(self, *args, **options):

        version = Version.objects.filter(name="João Ferreira de Almeida Atualizada")

        if not version.exists():
            version = Version()
            version.name = "João Ferreira de Almeida Atualizada"
            version.save()
        else:
            version = version.first()

        cod = "jfa"

        books = [
            { "book_id": 1, "site": "https://bibliaportugues.com/{}/genesis/".format(cod), "chapters": 51 },
            { "book_id": 2, "site": "https://bibliaportugues.com/{}/exodus/".format(cod), "chapters": 41 },
            { "book_id": 3, "site": "https://bibliaportugues.com/{}/leviticus/".format(cod), "chapters": 28 },
            { "book_id": 4, "site": "https://bibliaportugues.com/{}/numbers/".format(cod), "chapters": 37 },
            { "book_id": 5, "site": "https://bibliaportugues.com/{}/deuteronomy/".format(cod), "chapters": 35 },
            { "book_id": 6, "site": "https://bibliaportugues.com/{}/joshua/".format(cod), "chapters": 25 },
            { "book_id": 7, "site": "https://bibliaportugues.com/{}/judges/".format(cod), "chapters": 22 },
            { "book_id": 8, "site": "https://bibliaportugues.com/{}/ruth/".format(cod), "chapters": 5 },
            { "book_id": 9, "site": "https://bibliaportugues.com/{}/1_samuel/".format(cod), "chapters": 32 },
            { "book_id": 10, "site": "https://bibliaportugues.com/{}/2_samuel/".format(cod), "chapters": 25 },
            { "book_id": 11, "site": "https://bibliaportugues.com/{}/1_kings/".format(cod), "chapters": 23 },
            { "book_id": 12, "site": "https://bibliaportugues.com/{}/2_kings/".format(cod), "chapters": 26 },
            { "book_id": 13, "site": "https://bibliaportugues.com/{}/1_chronicles/".format(cod), "chapters": 30 },
            { "book_id": 14, "site": "https://bibliaportugues.com/{}/2_chronicles/".format(cod), "chapters": 37 },
            { "book_id": 15, "site": "https://bibliaportugues.com/{}/ezra/".format(cod), "chapters": 11 },
            { "book_id": 16, "site": "https://bibliaportugues.com/{}/nehemiah/".format(cod), "chapters": 14 },
            { "book_id": 17, "site": "https://bibliaportugues.com/{}/esther/".format(cod), "chapters": 11 },
            { "book_id": 18, "site": "https://bibliaportugues.com/{}/job/".format(cod), "chapters": 43 },
            { "book_id": 19, "site": "https://bibliaportugues.com/{}/psalms/".format(cod), "chapters": 151 },
            { "book_id": 20, "site": "https://bibliaportugues.com/{}/proverbs/".format(cod), "chapters": 32 },
            { "book_id": 21, "site": "https://bibliaportugues.com/{}/ecclesiastes/".format(cod), "chapters": 13 },
            { "book_id": 22, "site": "https://bibliaportugues.com/{}/songs/".format(cod), "chapters": 9 },
            { "book_id": 23, "site": "https://bibliaportugues.com/{}/isaiah/".format(cod), "chapters": 67 },
            { "book_id": 24, "site": "https://bibliaportugues.com/{}/jeremiah/".format(cod), "chapters": 53 },
            { "book_id": 25, "site": "https://bibliaportugues.com/{}/lamentations/".format(cod), "chapters": 6 },
            { "book_id": 26, "site": "https://bibliaportugues.com/{}/ezekiel/".format(cod), "chapters": 49 },
            { "book_id": 27, "site": "https://bibliaportugues.com/{}/daniel/".format(cod), "chapters": 13 },
            { "book_id": 28, "site": "https://bibliaportugues.com/{}/hosea/".format(cod), "chapters": 15 },
            { "book_id": 29, "site": "https://bibliaportugues.com/{}/joel/".format(cod), "chapters": 4 },
            { "book_id": 30, "site": "https://bibliaportugues.com/{}/amos/".format(cod), "chapters": 10 },
            { "book_id": 31, "site": "https://bibliaportugues.com/{}/obadiah/".format(cod), "chapters": 2 },
            { "book_id": 32, "site": "https://bibliaportugues.com/{}/jonah/".format(cod), "chapters": 5 },
            { "book_id": 33, "site": "https://bibliaportugues.com/{}/micah/".format(cod), "chapters": 8 },
            { "book_id": 34, "site": "https://bibliaportugues.com/{}/nahum/".format(cod), "chapters": 4 },
            { "book_id": 35, "site": "https://bibliaportugues.com/{}/habakkuk/".format(cod), "chapters": 4 },
            { "book_id": 36, "site": "https://bibliaportugues.com/{}/zephaniah/".format(cod), "chapters": 4 },
            { "book_id": 37, "site": "https://bibliaportugues.com/{}/haggai/".format(cod), "chapters": 3 },
            { "book_id": 38, "site": "https://bibliaportugues.com/{}/zechariah/".format(cod), "chapters": 15 },
            { "book_id": 39, "site": "https://bibliaportugues.com/{}/malachi/".format(cod), "chapters": 5 },

            { "book_id": 40, "site": "https://bibliaportugues.com/{}/matthew/".format(cod), "chapters": 29 },
            { "book_id": 41, "site": "https://bibliaportugues.com/{}/mark/".format(cod), "chapters": 17 },
            { "book_id": 42, "site": "https://bibliaportugues.com/{}/luke/".format(cod), "chapters": 25 },
            { "book_id": 43, "site": "https://bibliaportugues.com/{}/john/".format(cod), "chapters": 22 },
            { "book_id": 44, "site": "https://bibliaportugues.com/{}/acts/".format(cod), "chapters": 29 },
            { "book_id": 45, "site": "https://bibliaportugues.com/{}/romans/".format(cod), "chapters": 17 },
            { "book_id": 46, "site": "https://bibliaportugues.com/{}/1_corinthians/".format(cod), "chapters": 17 },
            { "book_id": 47, "site": "https://bibliaportugues.com/{}/2_corinthians/".format(cod), "chapters": 14 },
            { "book_id": 48, "site": "https://bibliaportugues.com/{}/galatians/".format(cod), "chapters": 7 },
            { "book_id": 49, "site": "https://bibliaportugues.com/{}/ephesians/".format(cod), "chapters": 7 },
            { "book_id": 50, "site": "https://bibliaportugues.com/{}/philippians/".format(cod), "chapters": 5 },
            { "book_id": 51, "site": "https://bibliaportugues.com/{}/colossians/".format(cod), "chapters": 5 },
            { "book_id": 52, "site": "https://bibliaportugues.com/{}/1_thessalonians/".format(cod), "chapters": 6 },
            { "book_id": 53, "site": "https://bibliaportugues.com/{}/2_thessalonians/".format(cod), "chapters": 4 },
            { "book_id": 54, "site": "https://bibliaportugues.com/{}/1_timothy/".format(cod), "chapters": 7 },
            { "book_id": 55, "site": "https://bibliaportugues.com/{}/2_timothy/".format(cod), "chapters": 5 },
            { "book_id": 56, "site": "https://bibliaportugues.com/{}/titus/".format(cod), "chapters": 4 },
            { "book_id": 57, "site": "https://bibliaportugues.com/{}/philemon/".format(cod), "chapters": 2 },
            { "book_id": 58, "site": "https://bibliaportugues.com/{}/hebrews/".format(cod), "chapters": 14 },
            { "book_id": 59, "site": "https://bibliaportugues.com/{}/james/".format(cod), "chapters": 6 },
            { "book_id": 60, "site": "https://bibliaportugues.com/{}/1_peter/".format(cod), "chapters": 6 },
            { "book_id": 61, "site": "https://bibliaportugues.com/{}/2_peter/".format(cod), "chapters": 4 },
            { "book_id": 62, "site": "https://bibliaportugues.com/{}/1_john/".format(cod), "chapters": 6 },
            { "book_id": 63, "site": "https://bibliaportugues.com/{}/2_john/".format(cod), "chapters": 2 },
            { "book_id": 64, "site": "https://bibliaportugues.com/{}/3_john/".format(cod), "chapters": 2 },
            { "book_id": 65, "site": "https://bibliaportugues.com/{}/jude/".format(cod), "chapters": 2 },
            { "book_id": 66, "site": "https://bibliaportugues.com/{}/revelation/".format(cod), "chapters": 23 },
        ]
                    

        for book in tqdm(books, ascii=True):
            
            for chapter in tqdm(range(1, book["chapters"]), ascii=True):
                url = "{}{}.htm".format(book["site"], chapter)
                r = request("get", url)

                if r.encoding is None or r.encoding == 'ISO-8859-1':
                    r.encoding = r.apparent_encoding

                soup = BeautifulSoup(r.text, 'html.parser')

                versicles = soup.find_all(class_='maintext')

                i  = 1

                for ver in tqdm(versicles, ascii=True):
                    text_ver = self.contents_to_string(ver.contents)
                    finder = Versicle.objects.filter(version=version, book_id=book["book_id"], chapter=chapter, versicle=i)
                    if not finder.exists():
                        Versicle.objects.create(version=version, chapter=chapter, versicle=i, \
                                text=text_ver, book_id=book["book_id"])
                    # else:
                    #     finder = finder.first()
                    #     finder.text = text_ver
                    #     finder.save()

                    i = i + 1

        
