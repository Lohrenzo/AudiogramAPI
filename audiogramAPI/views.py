from django.shortcuts import get_object_or_404
from rest_framework import generics, status  # viewsets,
from rest_framework.parsers import JSONParser, MultiPartParser  # FormParser,
from rest_framework.permissions import (  # DjangoModelPermissions,; DjangoModelPermissionsOrAnonReadOnly,
    AllowAny,
    IsAdminUser,
    IsAuthenticated,
)
from rest_framework.response import Response

from .models import Album, Audio, Genre, Playlist

# from rest_framework.views import APIView
from .permission import AudioUserWritePermission, IsArtistPermission
from .serializers import (
    AlbumSerializer,
    AudioSerializer,
    GenreSerializer,
    PlaylistSerializer,
)


class AudioView(generics.ListCreateAPIView):
    parser_classes = [MultiPartParser]
    permission_classes = [
        # IsAuthenticated,
        # IsArtistPermission,
        AllowAny,
    ]
    queryset = Audio.publishedaudios.all()
    serializer_class = AudioSerializer
    # ordering_fields = [
    #     "artist",
    #     "producer",
    #     "album",
    #     "genre",
    # ]
    filterset_fields = [
        "artist",
        "producer",
        "album",
        "genre",
    ]
    search_fields = [
        "title",
        "genre__title",
    ]
    # The double underscore helps with searching in a nested field like genre.

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

    def post(self, request, format=None):
        print(request.data)
        serializer = AudioSerializer(
            data=request.data,
            context=self.get_serializer_context(),
        )
        if serializer.is_valid():
            audio = serializer.save()
            return Response(
                f"Audio '{audio.title}' has been added.",
                status=status.HTTP_200_OK,
                content_type="text/plain",
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


class AudioDetail(
    generics.RetrieveUpdateDestroyAPIView,
    AudioUserWritePermission,
):
    permission_classes = [AudioUserWritePermission]
    parser_classes = [MultiPartParser]
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer


class LikesView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AudioSerializer
    # parser_classes = [MultiPartParser]

    def get_queryset(self):
        return Audio.objects.filter(likes=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
            content_type="application/json",
        )

    def create(self, request, *args, **kwargs):
        audio_id = request.data.get("audioId")
        audio = get_object_or_404(Audio, id=audio_id)
        if audio.likes.filter(id=request.user.id).exists():
            return Response(
                {"detail": "This audio is already liked by the user."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        audio.likes.add(request.user)
        serializer = self.get_serializer(audio)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GenreView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Genre.objects.all()
    parser_classes = [JSONParser]
    serializer_class = GenreSerializer

    def post(self, request):
        print(request.data)
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            genre = serializer.save()
            return Response(
                f"Genre '{genre.title}' has been added.",
                status=status.HTTP_200_OK,
                content_type="text/plain",
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


class AlbumView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Album.objects.all()
    parser_classes = [MultiPartParser]
    serializer_class = AlbumSerializer

    def post(self, request):
        print(request.data)
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            album = serializer.save()
            return Response(
                f"Genre '{album.title}' has been added.",
                status=status.HTTP_200_OK,
                content_type="text/plain",
            )

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


class PlaylistView(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    parser_classes = [MultiPartParser, JSONParser]
    serializer_class = PlaylistSerializer
    permission_classes = [AllowAny]

    # def get_permissions(self):
    #     if self.request.method == "GET":
    #         return [AllowAny()]
    #     return [IsAuthenticated()]

    def post(self, request):
        print(request.data)
        serializer = PlaylistSerializer(data=request.data)
        if serializer.is_valid():
            playlist = serializer.save()
            return Response(
                f"Genre '{playlist.title}' created.",
                status=status.HTTP_200_OK,
                content_type="text/plain",
            )

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


class PlaylistDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser, JSONParser]
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
