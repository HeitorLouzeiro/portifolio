# Generated by Django 4.1 on 2022-09-22 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0003_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmedia',
            name='skills',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='link',
            field=models.CharField(max_length=100),
        ),
    ]
