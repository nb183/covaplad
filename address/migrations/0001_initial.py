# Generated by Django 3.1.2 on 2020-10-17 13:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Country",
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
                ("name", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="District",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Municipality",
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
                ("name", models.CharField(max_length=100)),
                (
                    "district",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="address.district",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Ward",
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
                ("number", models.PositiveSmallIntegerField()),
                (
                    "municipality",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="address.municipality",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Province",
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
                ("name", models.CharField(max_length=100)),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="address.country",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="district",
            name="province",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="address.province"
            ),
        ),
        migrations.AddConstraint(
            model_name="ward",
            constraint=models.UniqueConstraint(
                fields=("number", "municipality"), name="unique_number_municiplaity"
            ),
        ),
        migrations.AddConstraint(
            model_name="province",
            constraint=models.UniqueConstraint(
                fields=("name", "country"), name="unique_name_country"
            ),
        ),
        migrations.AddConstraint(
            model_name="municipality",
            constraint=models.UniqueConstraint(
                fields=("name", "district"), name="unique_name_district"
            ),
        ),
        migrations.AddConstraint(
            model_name="district",
            constraint=models.UniqueConstraint(
                fields=("name", "province"), name="unique_name_province"
            ),
        ),
    ]
