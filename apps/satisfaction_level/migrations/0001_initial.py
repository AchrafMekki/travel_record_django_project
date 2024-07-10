# Generated by Django 5.0.6 on 2024-07-10 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SatisfactionLevel",
            fields=[
                (
                    "satisfaction_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    "satisfaction_value",
                    models.CharField(
                        choices=[
                            ("Very Unsatisfied", "Very Unsatisfied"),
                            ("Unsatisfied", "Unsatified"),
                            ("Neutral", "Neutral"),
                            ("Satisfied", "Satisfied"),
                            ("Very Satisfied", "Very Satisfied"),
                        ],
                        default="Neutral",
                        max_length=20,
                    ),
                ),
            ],
        ),
    ]
