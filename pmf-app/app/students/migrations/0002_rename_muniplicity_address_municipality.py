# Generated by Django 4.0.2 on 2023-01-23 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='muniplicity',
            new_name='municipality',
        ),
    ]
