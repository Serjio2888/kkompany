# Generated by Django 2.2.6 on 2019-12-09 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_answers_right_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.CharField(default='qwertyqwerty', max_length=32, verbose_name="parol'"),
        ),
        migrations.AlterField(
            model_name='answers',
            name='right_answer',
            field=models.BooleanField(default='wrong', verbose_name='верный ответ'),
        ),
    ]
