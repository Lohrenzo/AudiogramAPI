from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserRegistrationSerializer


class UserRegistration(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        print(request.data)

        register_serializer = UserRegistrationSerializer(data=request.data)
        if register_serializer.is_valid():
            user = register_serializer.save()
            if user:
                return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(register_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
