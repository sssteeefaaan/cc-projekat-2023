# Generated by Django 4.0.2 on 2023-01-23 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('username', models.CharField(db_index=True, max_length=20, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('email', models.CharField(db_index=True, max_length=50, unique=True)),
                ('umcn', models.CharField(db_index=True, max_length=13, unique=True)),
                ('idCardNumber', models.CharField(db_index=True, max_length=14, unique=True)),
                ('phoneNumber', models.CharField(db_index=True, max_length=14, unique=True)),
                ('image', models.ImageField(upload_to='images/professors')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.address')),
                ('faculty', models.ManyToManyField(blank=True, null=True, to='home.Faculty')),
            ],
        ),
    ]