# from account.models import User
from django.conf import settings
from django.db import models
from django.dispatch import receiver
from django.shortcuts import get_object_or_404

# from django.db.models.signals import pre_save
# from .helpers import get_audio_length
from .validators import (
    validate_cover_image_size,
    validate_image_file_extension,
)


def album_cover_upload_path(instance, filename):
    return f"{instance.id}/album_covers/{filename}"


def audio_cover_upload_path(instance, filename):
    return f"{instance.id}/audio_covers/{filename}"


def audio_file_upload_path(instance, filename):
    return f"{instance.id}/audios/{filename}"


class Genre(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Genres"

    def __str__(self) -> str:
        return self.title


class Album(models.Model):
    # id = models.Index
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    artist = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="album_artist",
    )
    cover = models.ImageField(
        null=True,
        blank=True,
        upload_to=album_cover_upload_path,
        validators=[validate_cover_image_size, validate_image_file_extension],
    )
    published = models.DateTimeField(auto_now_add=True)

    # slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.id:
            existing = get_object_or_404(Album, id=self.id)
            if existing.cover != self.cover:
                existing.cover.delete(save=False)
        super(Album, self).save(*args, **kwargs)

    @receiver(models.signals.pre_delete, sender="audiogramAPI.Album")
    def album_delete_files(sender, instance, **kwargs):
        for field in instance._meta.fields:
            if field.name == "cover":
                file = getattr(instance, field.name)
                if file:
                    file.delete(save=False)

    def __str__(self) -> str:
        return self.title


class Audio(models.Model):
    class PublishedAudios(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status="published")

    options = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    title = models.CharField(max_length=255)
    artist = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="audio_artist",
    )
    producer = models.CharField(max_length=255)
    audio = models.FileField(upload_to=audio_file_upload_path)
    cover = models.ImageField(
        null=True,
        blank=True,
        upload_to=audio_cover_upload_path,
        validators=[validate_cover_image_size, validate_image_file_extension],
    )
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name="audio_album",
    )
    published = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    # time_length = models.DecimalField(
    #     blank=True,
    #     max_digits=30,
    #     decimal_places=2,
    # )
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="likes",
        default=None,
        blank=True,
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        related_name="audio_genre",
    )
    status = models.CharField(
        max_length=10,
        choices=options,
        default="published",
    )
    objects = models.Manager()  # default manager
    publishedaudios = PublishedAudios()  # custom manager

    def save(self, *args, **kwargs):
        # if not self.time_length:
        #     # pass
        #     audio_length = get_audio_length()
        #     self.time_length = audio_length

        if self.id:
            existing = get_object_or_404(Audio, id=self.id)
            if existing.cover != self.cover:
                existing.cover.delete(save=False)
            if existing.audio != self.audio:
                existing.audio.delete(save=False)
        # return super().save(*args, **kwargs)
        super(Audio, self).save(*args, **kwargs)

    @receiver(models.signals.pre_delete, sender="audiogramAPI.Audio")
    def audio_delete_files(sender, instance, **kwargs):
        for field in instance._meta.fields:
            if field.name == "cover" or field.name == "audio":
                file = getattr(instance, field.name)
                if file:
                    file.delete(save=False)

    class Meta:
        verbose_name_plural = "Audios"
        ordering = (
            "title",
            "genre",
            "producer",
            "published",
        )

    def __str__(self) -> str:
        return f"{self.title} by {self.artist}"


class Playlist(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="playlist_creator",
    )
    audios = models.ManyToManyField(Audio, related_name="playlist_audios")

    class Meta:
        verbose_name_plural = "Playlists"

    def __str__(self) -> str:
        return self.title
