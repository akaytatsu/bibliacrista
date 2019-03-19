from django.db import models
from library.django_fulltext_search import SearchManager


class Testamentos(models.Model):
    tes_id = models.AutoField(primary_key=True)
    tes_nome = models.CharField(max_length=30)

    class Meta:
        db_table = 'testamentos'

class Versoes(models.Model):
    vrs_id = models.AutoField(primary_key=True)
    vrs_nome = models.CharField(max_length=50)

    class Meta:
        db_table = 'versoes'

class Livros(models.Model):
    liv_id = models.AutoField(primary_key=True)
    liv_tes = models.ForeignKey("biblia.Testamentos", verbose_name=u"testamentos", on_delete=models.CASCADE)
    liv_posicao = models.PositiveIntegerField()
    liv_nome = models.CharField(max_length=30)

    class Meta:
        db_table = 'livros'
        unique_together = (('liv_tes', 'liv_posicao'),)
        
class Versiculos(models.Model):

    objects    = SearchManager(['ver_texto',])


    ver_id = models.AutoField(primary_key=True)
    ver_vrs = models.ForeignKey("biblia.Versoes", verbose_name=u"Versão", on_delete=models.CASCADE)
    ver_liv = models.ForeignKey("biblia.Livros", verbose_name=u"Livros", on_delete=models.CASCADE)
    ver_capitulo = models.PositiveIntegerField()
    ver_versiculo = models.PositiveIntegerField()
    ver_texto = models.TextField()
    dicionario = models.ManyToManyField("biblia.Dicionario",)

    class Meta:
        db_table = 'versiculos'

class Dicionario(models.Model):
    palavra = models.CharField(max_length=70, null=False, blank=False)
    significado = models.TextField(null=False, blank=False)

    class Meta:
        db_table = 'dicionario'

    def __str__(self):
        return self.palavra
