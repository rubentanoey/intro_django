# Generated by Django 4.1 on 2022-09-27 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mytasks',
            old_name='review',
            new_name='description',
        ),
    ]