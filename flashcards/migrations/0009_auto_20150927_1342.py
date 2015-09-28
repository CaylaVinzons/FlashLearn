# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0008_documentcard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scan',
            name='scan_data',
            field=models.ImageField(upload_to='flashcards/static/scans/'),
        ),
    ]
