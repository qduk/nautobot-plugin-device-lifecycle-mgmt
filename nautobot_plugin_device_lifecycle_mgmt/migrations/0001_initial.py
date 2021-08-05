# Generated by Django 3.1.13 on 2021-08-04 20:04

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("dcim", "0005_device_local_context_schema"),
    ]

    operations = [
        migrations.CreateModel(
            name="HardwareLCM",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("created", models.DateField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                ("inventory_item", models.CharField(blank=True, max_length=255, null=True)),
                ("release_date", models.DateField(blank=True, null=True)),
                ("end_of_sale", models.DateField(blank=True, null=True)),
                ("end_of_support", models.DateField(blank=True, null=True)),
                ("end_of_sw_releases", models.DateField(blank=True, null=True)),
                ("end_of_security_patches", models.DateField(blank=True, null=True)),
                ("documentation_url", models.URLField(blank=True)),
                ("comments", models.TextField(blank=True, null=True)),
                (
                    "device_type",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="dcim.devicetype"
                    ),
                ),
            ],
            options={
                "ordering": ("end_of_support", "end_of_sale"),
            },
        ),
        migrations.AddConstraint(
            model_name="hardwarelcm",
            constraint=models.UniqueConstraint(fields=("device_type",), name="unique_device_type"),
        ),
        migrations.AddConstraint(
            model_name="hardwarelcm",
            constraint=models.UniqueConstraint(fields=("inventory_item",), name="unique_inventory_item_part"),
        ),
    ]
