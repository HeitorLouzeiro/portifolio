# Generated by Django 4.1 on 2022-10-19 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0018_alter_card_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='cover',
            field=models.ImageField(blank=True, upload_to='portifolio/projects/cover/'),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='cover',
            field=models.ImageField(blank=True, upload_to='portifolio/user/cover/'),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='pdf',
            field=models.FileField(blank=True, upload_to='portifolio/user/pdf/'),
        ),
    ]
