# Generated by Django 2.1.5 on 2019-03-19 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblia', '0003_dicionario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dicionario',
            name='ver',
        ),
        migrations.AlterField(
            model_name='dicionario',
            name='significado',
            field=models.TextField(),
        ),
    ]
