from rest_framework import generics, status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import (
    SAFE_METHODS,
    AllowAny,
    BasePermission,
    DjangoModelPermissions,
    DjangoModelPermissionsOrAnonReadOnly,
    IsAdminUser,
    IsAuthenticated,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Album, Audio, Genre
from .serializers import AudioSerializer


class AudioUserWritePermission(BasePermission):
    message = "Editing audios is 'Restricted' to the artist only."

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.artist == request.user


class AudioList(generics.ListAPIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [AllowAny]
    queryset = Audio.publishedaudios.all()
    serializer_class = AudioSerializer


class AudioDetail(
    generics.RetrieveUpdateDestroyAPIView,
    AudioUserWritePermission,
):
    permission_classes = [AudioUserWritePermission]
    parser_classes = [MultiPartParser, FormParser]
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer


class AudioCreate(generics.CreateAPIView):
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = AudioSerializer

    def post(self, request, format=None):
        print(request.data)
        serializer = AudioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
