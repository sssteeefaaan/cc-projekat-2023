# Generated by Django 4.0.2 on 2023-01-24 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_remove_faculty_address_alter_parent_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(default='images/students/default.jpg', upload_to='images/students'),
        ),
    ]