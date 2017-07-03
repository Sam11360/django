# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_auto_20170703_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='restaurant',
            field=models.ForeignKey(default='', to='menu.Restaurant'),
            preserve_default=False,
        ),
    ]
