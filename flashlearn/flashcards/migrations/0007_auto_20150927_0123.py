# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0006_auto_20150927_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdocument',
            name='user_id',
            field=models.CharField(max_length=10),
        ),
    ]
