# Generated by Django 2.2.6 on 2019-12-09 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20191209_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='tags',
            name='questions',
            field=models.ManyToManyField(blank=True, related_name='quest', to='main.Questions', verbose_name='Voprosi'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='main.Tags', verbose_name='Теги'),
        ),
    ]
