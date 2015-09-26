# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0004_auto_20150926_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDocument',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('document', models.ForeignKey(to='flashcards.Document')),
            ],
        ),
    ]
