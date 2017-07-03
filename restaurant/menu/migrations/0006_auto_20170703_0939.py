# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_auto_20170703_0937'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categorie',
            new_name='Restaurant',
        ),
    ]
