# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0003_problem_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worksheettranslation',
            name='problem',
        ),
        migrations.AddField(
            model_name='worksheet',
            name='problem',
            field=models.ManyToManyField(to='tools.Problem'),
        ),
    ]
