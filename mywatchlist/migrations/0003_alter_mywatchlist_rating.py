# Generated by Django 4.1 on 2022-09-21 16:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0002_alter_mywatchlist_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mywatchlist',
            name='rating',
            field=models.FloatField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]