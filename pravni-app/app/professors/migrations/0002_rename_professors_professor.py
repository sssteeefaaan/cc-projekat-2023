# Generated by Django 4.0.2 on 2023-01-24 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
        ('professors', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Professors',
            new_name='Professor',
        ),
    ]
