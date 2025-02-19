# Generated by Django 3.2.16 on 2023-02-07 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('segments', '0017_update_historical_segment_with_missing_changes'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalsegment',
            name='deleted_at',
            field=models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='segment',
            name='deleted_at',
            field=models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True),
        ),
    ]
