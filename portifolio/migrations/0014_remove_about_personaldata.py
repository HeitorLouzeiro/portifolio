# Generated by Django 4.1 on 2022-10-09 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0013_rename_socialmedia_minicard'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='personaldata',
        ),
    ]