# Generated by Django 5.0.6 on 2024-07-09 11:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("itau_app", "0006_alter_blogpost_tags"),
    ]

    operations = [
        migrations.AddField(
            model_name="companyinfo",
            name="email",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="tags",
            field=models.ManyToManyField(blank=True, to="itau_app.tag"),
        ),
    ]
