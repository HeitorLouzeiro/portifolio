# Generated by Django 4.1 on 2022-09-22 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0006_card'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='subtititle',
            new_name='subtitle',
        ),
    ]