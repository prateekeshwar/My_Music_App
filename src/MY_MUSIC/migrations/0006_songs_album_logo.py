# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MY_MUSIC', '0005_auto_20170503_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='album_logo',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d/', blank=True),
        ),
    ]
