# Generated by Django 3.1.3 on 2020-11-08 08:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("donor", "0006_auto_20201108_1146"),
    ]

    operations = [
        migrations.AlterField(
            model_name="donor",
            name="weight",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=5,
                validators=[django.core.validators.MinValueValidator(0.02)],
                verbose_name="weight (in kg)",
            ),
        ),
    ]
