# Generated by Django 3.1.3 on 2020-11-08 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0006_auto_20201108_1146"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="gender",
            field=models.CharField(
                choices=[
                    ("M", "Male"),
                    ("F", "Female"),
                    ("L", "Lesbian"),
                    ("G", "Gay"),
                    ("B", "Bisexual"),
                    ("T", "Transgender"),
                    ("N", "Prefer Not To Say"),
                ],
                max_length=1,
            ),
        ),
    ]
