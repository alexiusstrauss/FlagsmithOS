# Generated by Django 3.2.23 on 2023-11-16 16:01

from django.db import migrations


def create_default_subscription(apps, schema_editor):  # type: ignore[no-untyped-def]
    Organisation = apps.get_model("organisations", "Organisation")
    Subscription = apps.get_model("organisations", "Subscription")

    organisations_without_subscription = Organisation.objects.filter(
        subscription__isnull=True
    )

    subscriptions_to_create = []
    for organisation in organisations_without_subscription:
        subscriptions_to_create.append(Subscription(organisation=organisation))

    Subscription.objects.bulk_create(subscriptions_to_create)


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0047_organisation_force_2fa'),
    ]

    operations = [
        migrations.RunPython(
            create_default_subscription,
            reverse_code=migrations.RunPython.noop,
        )
    ]
