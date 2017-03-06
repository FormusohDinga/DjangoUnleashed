# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0006_newslink_unique_together_slug_startup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='tags',
            field=models.ManyToManyField(blank=True, to='organizer.Tag'),
        ),
    ]
