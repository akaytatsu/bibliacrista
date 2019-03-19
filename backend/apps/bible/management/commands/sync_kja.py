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

        version = Version.objects.filter(name="King James Atualizada")

        if not version.exists():
            version = Version()
            version.name = "King James Atualizada"
            version = version.save()
        else:
            version = version.first()

        books = [
            { "book_id": 1, "site": "https://bibliaportugues.com/kja/genesis/", "chapters": 51 },
            { "book_id": 2, "site": "https://bibliaportugues.com/kja/exodus/", "chapters": 41 },
            { "book_id": 3, "site": "https://bibliaportugues.com/kja/leviticus/", "chapters": 28 },
            { "book_id": 4, "site": "https://bibliaportugues.com/kja/numbers/", "chapters": 37 },
            { "book_id": 5, "site": "https://bibliaportugues.com/kja/deuteronomy/", "chapters": 35 },
            { "book_id": 6, "site": "https://bibliaportugues.com/kja/joshua/", "chapters": 25 },
            { "book_id": 7, "site": "https://bibliaportugues.com/kja/judges/", "chapters": 22 },
            { "book_id": 8, "site": "https://bibliaportugues.com/kja/ruth/", "chapters": 5 },
            { "book_id": 9, "site": "https://bibliaportugues.com/kja/1_samuel/", "chapters": 32 },
            { "book_id": 10, "site": "https://bibliaportugues.com/kja/2_samuel/", "chapters": 25 },
            { "book_id": 11, "site": "https://bibliaportugues.com/kja/1_kings/", "chapters": 23 },
            { "book_id": 12, "site": "https://bibliaportugues.com/kja/2_kings/", "chapters": 26 },
            { "book_id": 13, "site": "https://bibliaportugues.com/kja/1_chronicles/", "chapters": 30 },
            { "book_id": 14, "site": "https://bibliaportugues.com/kja/2_chronicles/", "chapters": 37 },
            { "book_id": 15, "site": "https://bibliaportugues.com/kja/ezra/", "chapters": 11 },
            { "book_id": 16, "site": "https://bibliaportugues.com/kja/nehemiah/", "chapters": 14 },
            { "book_id": 17, "site": "https://bibliaportugues.com/kja/esther/", "chapters": 11 },
            { "book_id": 18, "site": "https://bibliaportugues.com/kja/job/", "chapters": 43 },
            { "book_id": 19, "site": "https://bibliaportugues.com/kja/psalms/", "chapters": 151 },
            { "book_id": 20, "site": "https://bibliaportugues.com/kja/proverbs/", "chapters": 32 },
            { "book_id": 21, "site": "https://bibliaportugues.com/kja/ecclesiastes/", "chapters": 13 },
            { "book_id": 22, "site": "https://bibliaportugues.com/kja/songs/", "chapters": 9 },
            { "book_id": 23, "site": "https://bibliaportugues.com/kja/isaiah/", "chapters": 67 },
            { "book_id": 24, "site": "https://bibliaportugues.com/kja/jeremiah/", "chapters": 53 },
            { "book_id": 25, "site": "https://bibliaportugues.com/kja/lamentations/", "chapters": 6 },
            { "book_id": 26, "site": "https://bibliaportugues.com/kja/ezekiel/", "chapters": 49 },
            { "book_id": 27, "site": "https://bibliaportugues.com/kja/daniel/", "chapters": 13 },
            { "book_id": 28, "site": "https://bibliaportugues.com/kja/hosea/", "chapters": 15 },
            { "book_id": 29, "site": "https://bibliaportugues.com/kja/joel/", "chapters": 4 },
            { "book_id": 30, "site": "https://bibliaportugues.com/kja/amos/", "chapters": 10 },
            { "book_id": 31, "site": "https://bibliaportugues.com/kja/obadiah/", "chapters": 2 },
            { "book_id": 32, "site": "https://bibliaportugues.com/kja/jonah/", "chapters": 5 },
            { "book_id": 33, "site": "https://bibliaportugues.com/kja/micah/", "chapters": 8 },
            { "book_id": 34, "site": "https://bibliaportugues.com/kja/nahum/", "chapters": 4 },
            { "book_id": 35, "site": "https://bibliaportugues.com/kja/habakkuk/", "chapters": 4 },
            { "book_id": 36, "site": "https://bibliaportugues.com/kja/zephaniah/", "chapters": 4 },
            { "book_id": 37, "site": "https://bibliaportugues.com/kja/haggai/", "chapters": 3 },
            { "book_id": 38, "site": "https://bibliaportugues.com/kja/zechariah/", "chapters": 15 },
            { "book_id": 39, "site": "https://bibliaportugues.com/kja/malachi/", "chapters": 5 },

            { "book_id": 40, "site": "https://bibliaportugues.com/kja/matthew/", "chapters": 29 },
            { "book_id": 41, "site": "https://bibliaportugues.com/kja/mark/", "chapters": 17 },
            { "book_id": 42, "site": "https://bibliaportugues.com/kja/luke/", "chapters": 25 },
            { "book_id": 43, "site": "https://bibliaportugues.com/kja/john/", "chapters": 22 },
            { "book_id": 44, "site": "https://bibliaportugues.com/kja/acts/", "chapters": 29 },
            { "book_id": 45, "site": "https://bibliaportugues.com/kja/romans/", "chapters": 17 },
            { "book_id": 46, "site": "https://bibliaportugues.com/kja/1_corinthians/", "chapters": 17 },
            { "book_id": 47, "site": "https://bibliaportugues.com/kja/2_corinthians/", "chapters": 14 },
            { "book_id": 48, "site": "https://bibliaportugues.com/kja/galatians/", "chapters": 7 },
            { "book_id": 49, "site": "https://bibliaportugues.com/kja/ephesians/", "chapters": 7 },
            { "book_id": 50, "site": "https://bibliaportugues.com/kja/philippians/", "chapters": 5 },
            { "book_id": 51, "site": "https://bibliaportugues.com/kja/colossians/", "chapters": 5 },
            { "book_id": 52, "site": "https://bibliaportugues.com/kja/1_thessalonians/", "chapters": 6 },
            { "book_id": 53, "site": "https://bibliaportugues.com/kja/2_thessalonians/", "chapters": 4 },
            { "book_id": 54, "site": "https://bibliaportugues.com/kja/1_timothy/", "chapters": 7 },
            { "book_id": 55, "site": "https://bibliaportugues.com/kja/2_timothy/", "chapters": 5 },
            { "book_id": 56, "site": "https://bibliaportugues.com/kja/titus/", "chapters": 4 },
            { "book_id": 57, "site": "https://bibliaportugues.com/kja/philemon/", "chapters": 2 },
            { "book_id": 58, "site": "https://bibliaportugues.com/kja/hebrews/", "chapters": 14 },
            { "book_id": 59, "site": "https://bibliaportugues.com/kja/james/", "chapters": 6 },
            { "book_id": 60, "site": "https://bibliaportugues.com/kja/1_peter/", "chapters": 6 },
            { "book_id": 61, "site": "https://bibliaportugues.com/kja/2_peter/", "chapters": 4 },
            { "book_id": 62, "site": "https://bibliaportugues.com/kja/1_john/", "chapters": 6 },
            { "book_id": 63, "site": "https://bibliaportugues.com/kja/2_john/", "chapters": 2 },
            { "book_id": 64, "site": "https://bibliaportugues.com/kja/3_john/", "chapters": 2 },
            { "book_id": 65, "site": "https://bibliaportugues.com/kja/jude/", "chapters": 2 },
            { "book_id": 66, "site": "https://bibliaportugues.com/kja/revelation/", "chapters": 23 },
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

        
