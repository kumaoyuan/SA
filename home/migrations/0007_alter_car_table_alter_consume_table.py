# Generated by Django 4.1.5 on 2023-01-05 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0006_car_consume"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="car",
            table="car",
        ),
        migrations.AlterModelTable(
            name="consume",
            table="consume",
        ),
    ]
