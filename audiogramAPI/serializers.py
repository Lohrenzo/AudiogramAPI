# from django.conf.global_settings import AUTH_USER_MODEL
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from account.models import User

from .models import Album, Audio, Genre


class GenreSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    description = serializers.CharField(default="")

    class Meta:
        model = Genre
        fields = "__all__"


class AlbumSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    description = serializers.CharField(default="")
    artist = serializers.SlugRelatedField(
        # queryset=AUTH_USER_MODEL.objects.all(),
        queryset=User.objects.all(),
        slug_field="username",
    )
    cover = serializers.ImageField(allow_empty_file=True)

    class Meta:
        model = Album
        fields = "__all__"


class AudioSerializer(serializers.ModelSerializer):
    # genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all())
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field="title",
    )
    album = serializers.SlugRelatedField(
        queryset=Album.objects.all(),
        slug_field="title",
    )
    artist = serializers.SlugRelatedField(
        # queryset=AUTH_USER_MODEL.objects.all(),
        queryset=User.objects.all(),
        slug_field="username",
    )
    title = serializers.CharField(
        required=True,
        max_length=255,
        validators=[
            UniqueValidator(queryset=Audio.objects.all()),
        ],
    )  # Unique Validator for title. 1st Method
    published = serializers.DateTimeField(read_only=True)
    edited = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Audio
        fields = (
            "id",
            "title",
            "artist",
            "artist",
            "producer",
            "audio",
            "cover",
            "album",
            "status",
            "likes",
            "genre",
            "edited",
            "published",
        )
