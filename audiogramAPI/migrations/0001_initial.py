# Generated by Django 4.2.4 on 2023-11-05 02:58

import audiogramAPI.models
import audiogramAPI.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Album",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "cover",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=audiogramAPI.models.album_cover_upload_path,
                        validators=[
                            audiogramAPI.validators.validate_cover_image_size,
                            audiogramAPI.validators.validate_image_file_extension,
                        ],
                    ),
                ),
                (
                    "artist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="album_artist",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
            ],
            options={
                "verbose_name_plural": "Genres",
            },
        ),
        migrations.CreateModel(
            name="Audio",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("producer", models.CharField(max_length=255)),
                (
                    "audio",
                    models.FileField(
                        upload_to=audiogramAPI.models.audio_file_upload_path
                    ),
                ),
                (
                    "cover",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=audiogramAPI.models.audio_cover_upload_path,
                        validators=[
                            audiogramAPI.validators.validate_cover_image_size,
                            audiogramAPI.validators.validate_image_file_extension,
                        ],
                    ),
                ),
                ("published", models.DateTimeField(auto_now_add=True)),
                ("edited", models.DateTimeField(auto_now=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("draft", "Draft"), ("published", "Published")],
                        default="published",
                        max_length=10,
                    ),
                ),
                (
                    "album",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="audio_album",
                        to="audiogramAPI.album",
                    ),
                ),
                (
                    "artist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="audio_artist",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "genre",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="audio_genre",
                        to="audiogramAPI.genre",
                    ),
                ),
                (
                    "likes",
                    models.ManyToManyField(
                        blank=True, related_name="likes", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Audios",
                "ordering": ("title",),
            },
        ),
    ]
