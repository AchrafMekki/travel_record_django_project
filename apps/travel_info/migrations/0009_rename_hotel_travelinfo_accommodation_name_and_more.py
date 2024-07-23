# Generated by Django 5.0.6 on 2024-07-23 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("travel_info", "0008_alter_travelinfo_total_duration"),
    ]

    operations = [
        migrations.RenameField(
            model_name="travelinfo",
            old_name="hotel",
            new_name="accommodation_name",
        ),
        migrations.AddField(
            model_name="travelinfo",
            name="accommodation_type",
            field=models.CharField(
                choices=[
                    ("Hotel", "Hotel"),
                    ("Airbnb", "Airbnb"),
                    ("Hostel", "Hostel"),
                    ("Guesthouse", "Guesthouse"),
                    ("Other", "Other"),
                ],
                default="Hotel",
                max_length=15,
            ),
        ),
    ]
