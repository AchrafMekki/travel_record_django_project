# Generated by Django 5.0.6 on 2024-07-21 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("travel_info", "0002_satisfactionlevel_rename_year_travelinfo_date_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="travelinfo",
            old_name="tourist_id",
            new_name="tourist",
        ),
    ]
