from django.urls import path

from .views import AudioCreate, AudioDetail, AudioList

urlpatterns = [
    path("", AudioList.as_view(), name="list"),
    path("create", AudioCreate.as_view(), name="create"),
    path("<int:pk>", AudioDetail.as_view(), name="detail"),
]
