# Generated by Django 4.1 on 2022-09-22 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0007_rename_subtititle_card_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='cover',
            field=models.ImageField(
                blank=True, upload_to='portifolio/covers/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='cover',
            field=models.ImageField(
                blank=True, upload_to='portifolio/user/cover/%Y/%m/%d/'),
        ),
    ]
