# Generated by Django 3.1.4 on 2020-12-16 10:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("donation_venue", "0005_auto_20201108_1158"),
        ("donor", "0009_merge_20201108_1443"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="donor",
            name="test_report",
        ),
        migrations.AlterUniqueTogether(
            name="donorregistration",
            unique_together={("donor", "venue")},
        ),
        migrations.CreateModel(
            name="TestReport",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("report", models.ImageField(unique=True, upload_to="test_reports/")),
                (
                    "donor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="donor.donor"
                    ),
                ),
            ],
            options={
                "verbose_name": "Test Report",
            },
        ),
    ]
