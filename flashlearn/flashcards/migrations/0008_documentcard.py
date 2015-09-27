# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0007_auto_20150927_0123'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentCard',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('card', models.ForeignKey(to='flashcards.Card')),
                ('document', models.ForeignKey(to='flashcards.Document')),
            ],
        ),
    ]
