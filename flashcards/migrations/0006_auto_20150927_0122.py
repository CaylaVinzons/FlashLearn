# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0005_userdocument'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdocument',
            name='userid',
        ),
        migrations.AddField(
            model_name='userdocument',
            name='user_id',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
