# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-04 13:48
from __future__ import unicode_literals

from django.db import migrations

from ..models import Feature


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0004_auto_20180604_1259'),
    ]

    operations = [
        migrations.RunSQL(
            [("CREATE UNIQUE INDEX lowercase_feature_name ON " + Feature._meta.db_table +
              "(lower(name), project_id);")],
            [("DROP INDEX lowercase_feature_name;")],
        )
    ]