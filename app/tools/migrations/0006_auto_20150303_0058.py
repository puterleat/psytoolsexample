# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0005_auto_20150303_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worksheettranslation',
            name='pdf',
            field=models.FileField(null=True, upload_to=b'uploads', blank=True),
        ),
    ]
