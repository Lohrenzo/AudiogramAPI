# Generated by Django 4.2.4 on 2023-08-19 19:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("audiogramAPI", "0002_alter_album_title_alter_audio_title_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="audio",
            options={"ordering": ("title",), "verbose_name_plural": "Audios"},
        ),
    ]
