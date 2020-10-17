# Generated by Django 3.1.2 on 2020-10-17 13:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("address", "0001_initial"),
        ("donation_venue", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="donationvenue",
            name="address",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="address.ward",
            ),
            preserve_default=False,
        ),
    ]
