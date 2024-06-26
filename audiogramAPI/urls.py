from django.urls import path

from .views import (
    AudioView,
    AudioDetail,
    GenreView,
    AlbumView,
    PlaylistView,
    PlaylistDetail,
    LikesView,
)

urlpatterns = [
    path("audio", AudioView.as_view(), name="audio"),
    path(
        "audio/<int:pk>",
        AudioDetail.as_view(),
        name="audio_detail",
    ),
    path("genre", GenreView.as_view(), name="genre"),
    path("album", AlbumView.as_view(), name="album"),
    path("likes", LikesView.as_view(), name="likes"),
    path("playlist", PlaylistView.as_view(), name="playlist"),
    path(
        "playlist/<int:pk>",
        PlaylistDetail.as_view(),
        name="playlist_detail",
    ),
]
