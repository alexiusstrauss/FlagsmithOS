# Generated by Django 3.2.16 on 2022-11-25 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_project_feature_name_regex'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='deleted_at',
            field=models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True),
        ),
    ]
