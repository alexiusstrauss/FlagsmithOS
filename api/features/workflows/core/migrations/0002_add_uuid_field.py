# Generated by Django 3.2.13 on 2022-06-22 16:17

from django.db import migrations, models
import uuid

from core.migration_helpers import AddDefaultUUIDs


class Migration(migrations.Migration):

    dependencies = [
        ("workflows_core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="changerequest",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False, null=True),
        ),
        migrations.RunPython(
            AddDefaultUUIDs("workflows_core", "changerequest"),
            reverse_code=migrations.RunPython.noop,
        ),
        migrations.AlterField(
            model_name="changerequest",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
