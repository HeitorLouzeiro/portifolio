# Generated by Django 4.1 on 2022-09-26 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0009_alter_card_cover'),
    ]

    operations = [
        migrations.CreateModel(
            name='BarProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('progress', models.CharField(max_length=3)),
                ('personaldata', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='portifolio.personaldata')),
            ],
        ),
    ]
