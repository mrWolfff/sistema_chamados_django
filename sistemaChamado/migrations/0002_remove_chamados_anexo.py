# Generated by Django 2.0.13 on 2019-06-25 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaChamado', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chamados',
            name='anexo',
        ),
    ]
