# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app.tools.models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0006_auto_20150303_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worksheettranslation',
            name='pdf',
            field=models.FileField(storage=app.tools.models.MyS3BotoStorage(querystring_auth=True, bucket=b'psytools', acl=b'public-read'), null=True, upload_to=app.tools.models.worksheet_file_name, blank=True),
        ),
    ]
