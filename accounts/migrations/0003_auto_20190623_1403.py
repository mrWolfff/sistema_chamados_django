# Generated by Django 2.0.13 on 2019-06-23 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190622_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='../media'),
        ),
    ]
