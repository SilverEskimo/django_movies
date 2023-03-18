# Generated by Django 4.1.7 on 2023-03-15 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('birth_date', models.DateField()),
            ],
            options={
                'db_table': 'directors',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('year', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='movies_app.director')),
            ],
            options={
                'db_table': 'movies',
            },
        ),
    ]