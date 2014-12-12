# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('sito', '0004_auto_20141211_0400'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='intro',
            field=models.TextField(null=True, verbose_name=b'Intro', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='news',
            name='intro_uk',
            field=models.TextField(null=True, verbose_name=b'Intro Inglese', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='page',
            name='intro',
            field=models.TextField(null=True, verbose_name=b'Intro', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='page',
            name='intro_uk',
            field=models.TextField(null=True, verbose_name=b'Intro Inglese', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='intro',
            field=models.TextField(null=True, verbose_name=b'Intro', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='intro_uk',
            field=models.TextField(null=True, verbose_name=b'Intro Inglese', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='body',
            field=tinymce.models.HTMLField(null=True, verbose_name=b'Descrizione', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='body_uk',
            field=tinymce.models.HTMLField(null=True, verbose_name=b'Descrizione Inglese', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='body',
            field=tinymce.models.HTMLField(null=True, verbose_name=b'Descrizione', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='body_uk',
            field=tinymce.models.HTMLField(null=True, verbose_name=b'Descrizione Inglese', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='body_uk',
            field=tinymce.models.HTMLField(null=True, verbose_name=b'Descrizione Inglese', blank=True),
            preserve_default=True,
        ),
    ]
