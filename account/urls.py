from django.urls import path

from .views import ListenersView, ArtistsView

urlpatterns = [
    path(
        "register/listener",
        ListenersView.as_view(),
        name="register_listener",
    ),
    path(
        "register/artist",
        ArtistsView.as_view(),
        name="register_artist",
    ),
]
