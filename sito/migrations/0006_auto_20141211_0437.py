# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sito', '0005_auto_20141211_0409'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'News'},
        ),
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name_plural': 'Progetti'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': 'Post'},
        ),
    ]
