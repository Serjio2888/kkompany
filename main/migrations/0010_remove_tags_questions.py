# Generated by Django 2.2.6 on 2019-12-16 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20191209_1834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='questions',
        ),
    ]