# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('sito', '0003_auto_20141203_0429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=tinymce.models.HTMLField(null=True, verbose_name=b'Descrizione', blank=True),
            preserve_default=True,
        ),
    ]
