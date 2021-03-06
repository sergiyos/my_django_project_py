# Generated by Django 2.2.7 on 2019-11-16 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0002_auto_20191116_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_title', models.CharField(max_length=50, verbose_name='Назва групи')),
            ],
            options={
                'verbose_name': 'Група',
                'verbose_name_plural': 'Групи',
            },
        ),
        migrations.CreateModel(
            name='Practice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('practice_title', models.CharField(max_length=200, verbose_name='Назва практики')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')),
                ('start_date', models.DateTimeField(verbose_name='Дата початку практики')),
                ('end_date', models.DateTimeField(verbose_name='Дата закінчення практики')),
            ],
            options={
                'verbose_name': 'Практика',
                'verbose_name_plural': 'Практика',
            },
        ),
    ]
