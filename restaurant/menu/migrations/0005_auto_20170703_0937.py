# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20170703_0917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plat',
            name='categorie',
        ),
        migrations.AddField(
            model_name='plat',
            name='menu',
            field=models.ForeignKey(default='', to='menu.Menu'),
            preserve_default=False,
        ),
    ]
