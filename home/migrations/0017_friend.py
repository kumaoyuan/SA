# Generated by Django 4.1.5 on 2023-01-10 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0016_consume_piece"),
    ]

    operations = [
        migrations.CreateModel(
            name="friend",
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
                ("memberAc", models.CharField(max_length=10)),
                ("friendAc", models.CharField(max_length=10)),
            ],
            options={
                "db_table": "friend",
            },
        ),
    ]
