# Generated by Django 5.0.6 on 2024-07-27 13:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("itau_app", "0022_alter_aboutus_image_alter_blogpost_image_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="aboutus",
            name="imageauditors",
            field=models.ImageField(
                blank=True, null=True, upload_to="about_us_images/"
            ),
        ),
    ]