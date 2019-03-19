from django.db import models
from library.django_fulltext_search import SearchManager


class Testament(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'testament'

class Version(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'version'

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    testament = models.ForeignKey("bible.Testament", verbose_name=u"testament", on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'book'
        
class Versicle(models.Model):
    objects    = SearchManager(['text',])

    id = models.AutoField(primary_key=True)
    version = models.ForeignKey("bible.Version", verbose_name=u"Version", on_delete=models.CASCADE)
    book = models.ForeignKey("bible.Book", verbose_name=u"Book", on_delete=models.CASCADE)
    chapter = models.PositiveIntegerField()
    versicle = models.PositiveIntegerField()
    text = models.TextField()
    dictionary = models.ManyToManyField("bible.Dictionary",)

    class Meta:
        db_table = 'versicle'

class Dictionary(models.Model):
    term = models.CharField(max_length=70, null=False, blank=False)
    meaning = models.TextField(null=False, blank=False)

    class Meta:
        db_table = 'dictionary'

    def __str__(self):
        return self.term
