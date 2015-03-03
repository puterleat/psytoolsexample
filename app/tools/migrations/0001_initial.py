# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProblemTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=15, verbose_name='language', choices=[(b'en', b'English'), (b'de', b'German')])),
                ('name', models.CharField(max_length=255)),
                ('model', models.ForeignKey(related_name='translations', verbose_name=b'problem', to='tools.Problem')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Worksheet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WorksheetTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=15, verbose_name='language', choices=[(b'en', b'English'), (b'de', b'German')])),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('pdf', models.FileField(upload_to=b'')),
                ('model', models.ForeignKey(related_name='translations', verbose_name=b'worksheet', to='tools.Worksheet')),
                ('problem', models.ManyToManyField(to='tools.Problem')),
                ('tags', models.ManyToManyField(to='tools.Tag', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
