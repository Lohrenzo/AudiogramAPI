# from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import User
from .serializers import UserListenerSerializer, UserArtistSerializer


# class Users(APIView):
class ListenersView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserListenerSerializer

    def post(self, request):
        print(request.data)

        user_serializer = UserListenerSerializer(data=request.data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            if user:
                return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(
                user_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


class ArtistsView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserArtistSerializer

    def post(self, request):
        print(request.data)

        user_serializer = UserArtistSerializer(data=request.data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            if user:
                return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(
                user_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )
