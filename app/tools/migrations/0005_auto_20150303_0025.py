# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0004_auto_20150303_0014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='worksheet',
            old_name='problem',
            new_name='problems',
        ),
        migrations.AlterField(
            model_name='worksheettranslation',
            name='pdf',
            field=models.FileField(upload_to=b'uploads'),
        ),
    ]
