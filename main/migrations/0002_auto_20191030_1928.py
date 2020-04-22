# Generated by Django 2.2.6 on 2019-10-30 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='вопросы', to='main.Tags', verbose_name='Теги'),
        ),
        migrations.AlterField(
            model_name='tags',
            name='questions_count',
            field=models.IntegerField(default=0, verbose_name='вопросы'),
        ),
        migrations.DeleteModel(
            name='QuestTag',
        ),
    ]