# Generated by Django 4.2.4 on 2023-08-18 12:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("audiogramAPI", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="album",
            name="title",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="audio",
            name="title",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="genre",
            name="title",
            field=models.CharField(max_length=100),
        ),
    ]