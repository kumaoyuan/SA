# Generated by Django 4.1.5 on 2023-01-05 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0008_car_carev"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="carEv",
            field=models.IntegerField(default=0),
        ),
    ]