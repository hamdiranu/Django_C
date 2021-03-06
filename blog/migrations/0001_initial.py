# Generated by Django 3.0 on 2019-12-10 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gambar', models.CharField(max_length=200)),
                ('Title', models.CharField(max_length=200)),
                ('Content', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Mentee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gambar', models.CharField(max_length=200)),
                ('Name', models.CharField(max_length=200)),
                ('Quote', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gambar', models.CharField(max_length=200)),
                ('Nama', models.CharField(max_length=200)),
                ('Experience', models.CharField(max_length=200)),
                ('Quote', models.TextField(max_length=200)),
            ],
        ),
    ]
