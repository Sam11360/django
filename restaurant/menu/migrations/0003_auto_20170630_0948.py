# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_categorie_mmnu'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='mMnu',
            new_name='Plats',
        ),
    ]
