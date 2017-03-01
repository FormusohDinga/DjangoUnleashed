# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

TAGS = (
    # ( tag name, tag slug ),
    ("augmented reality", "augmented-reality"),
    ("big data", "big-data"),
    ("education", "education"),
    ("ipython", "ipython"),
    ("javascript", "javascript"),
    ("jupyter", "jupyter"),
    ("node.js", "node-js"),
    ("php", "php"),
    ("python", "python"),
    ("ruby on rails", "ruby-on-rails"),
    ("ruby", "ruby"),
)


def add_tag_data(apps, schema_editor):
    Tag = apps.get_model('organizer', 'Tag')
    for tag_name, tag_slug in TAGS:
        print(tag_slug)
        Tag.objects.create(
            name=tag_name,
            slug=tag_slug)


def remove_tag_data(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            add_tag_data,
            remove_tag_data)
    ]
