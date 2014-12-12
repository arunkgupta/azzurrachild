# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sito', '0006_auto_20141211_0437'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titolo', models.CharField(max_length=100, null=True, verbose_name=b'Titolo:', blank=True)),
                ('titolo_uk', models.CharField(max_length=100, null=True, verbose_name=b'Titolo Inglese:', blank=True)),
                ('email', models.CharField(max_length=100, null=True, verbose_name=b'Email:', blank=True)),
                ('url', models.CharField(max_length=100, null=True, verbose_name=b'Link:', blank=True)),
                ('body', models.TextField(null=True, verbose_name=b'Descrizione', blank=True)),
                ('body_uk', models.TextField(null=True, verbose_name=b'Descrizione Inglese', blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'uploaded_images', blank=True)),
                (b'miniatura', image_cropping.fields.ImageRatioField(b'image', '500x281', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='miniatura')),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
                'verbose_name_plural': 'News',
            },
            bases=(models.Model,),
        ),
    ]
