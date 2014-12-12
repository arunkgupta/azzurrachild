# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sito', '0002_slider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name=b'miniatura',
            field=image_cropping.fields.ImageRatioField(b'image', '300x200', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='miniatura'),
            preserve_default=True,
        ),
    ]
