# Generated by Django 5.0.6 on 2024-07-22 12:13

import storages.backends.s3
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("itau_app", "0020_alter_aboutus_image_alter_blogpost_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aboutus",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                storage=storages.backends.s3.S3Storage(),
                upload_to="about_us_images/",
            ),
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                storage=storages.backends.s3.S3Storage(),
                upload_to="blog_images/",
            ),
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="subImage",
            field=models.ImageField(
                blank=True,
                null=True,
                storage=storages.backends.s3.S3Storage(),
                upload_to="blog_images/",
            ),
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="subImage2",
            field=models.ImageField(
                blank=True,
                null=True,
                storage=storages.backends.s3.S3Storage(),
                upload_to="blog_images/",
            ),
        ),
        migrations.AlterField(
            model_name="companyinfo",
            name="brochure",
            field=models.FileField(
                blank=True,
                null=True,
                storage=storages.backends.s3.S3Storage(),
                upload_to="brochures/",
            ),
        ),
        migrations.AlterField(
            model_name="companyinfo",
            name="logo",
            field=models.ImageField(
                storage=storages.backends.s3.S3Storage(), upload_to="logos/"
            ),
        ),
        migrations.AlterField(
            model_name="companyinfo",
            name="logo_two",
            field=models.ImageField(
                storage=storages.backends.s3.S3Storage(), upload_to="logostwo/"
            ),
        ),
        migrations.AlterField(
            model_name="ourteam",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                storage=storages.backends.s3.S3Storage(),
                upload_to="ourTeam_images/",
            ),
        ),
        migrations.AlterField(
            model_name="partner",
            name="logo",
            field=models.ImageField(
                blank=True,
                null=True,
                storage=storages.backends.s3.S3Storage(),
                upload_to="partners/",
            ),
        ),
        migrations.AlterField(
            model_name="testimony",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                storage=storages.backends.s3.S3Storage(),
                upload_to="testimonials/",
            ),
        ),
    ]
