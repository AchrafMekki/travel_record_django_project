# Generated by Django 5.0.6 on 2024-07-23 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tourist_detail", "0003_alter_touristdetails_tourist"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="touristdetails",
            options={
                "verbose_name": "Tourist Detail",
                "verbose_name_plural": "Tourist Details",
            },
        ),
    ]
