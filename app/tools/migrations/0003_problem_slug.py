# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0002_remove_problem_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='slug',
            field=models.SlugField(default='anxiety'),
            preserve_default=False,
        ),
    ]
