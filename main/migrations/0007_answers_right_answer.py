# Generated by Django 2.2.6 on 2019-12-09 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_questions_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='right_answer',
            field=models.BooleanField(default=False, verbose_name='верный ответ'),
        ),
    ]
