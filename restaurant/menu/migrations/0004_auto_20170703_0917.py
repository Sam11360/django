# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20170630_0948'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Plats',
            new_name='Plat',
        ),
    ]
