# Generated by Django 4.1.5 on 2023-01-04 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_remove_member_memberid"),
    ]

    operations = [
        migrations.AddField(
            model_name="member",
            name="memberPt",
            field=models.IntegerField(default=0),
        ),
    ]
