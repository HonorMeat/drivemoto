# Generated by Django 3.2.4 on 2021-06-20 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20210620_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Цвет'),
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Вес'),
        ),
    ]
