# Generated by Django 3.2 on 2021-04-14 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faturalarapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faturalar',
            name='date',
            field=models.DateTimeField(blank=True),
        ),
    ]
