# Generated by Django 4.0.5 on 2022-06-16 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_user_permission_level"),
    ]

    operations = [
        migrations.CreateModel(
            name="Hobby",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="취미")),
            ],
        ),
    ]
