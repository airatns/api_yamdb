# Generated by Django 2.2.16 on 2022-05-11 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20220510_2036'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Category',
        ),
        migrations.RenameModel(
            old_name='Genres',
            new_name='Genre',
        ),
        migrations.RenameModel(
            old_name='Titles',
            new_name='Title',
        ),
    ]
