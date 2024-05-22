from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
)  # TokenRefreshSerializer,

# from rest_framework_simplejwt.state import token_backend


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)

        # Custom data you want to include
        user = self.user
        data.update({"username": user.username})
        data.update({"id": user.id})
        data.update(
            {
                "roles": {
                    "is_admin": user.is_admin,
                    "is_listener": user.is_listener,
                    "is_artist": user.is_artist,
                }
            }
        )
        # and everything else you want to send in the response
        return data


# class CustomTokenRefreshSerializer(TokenRefreshSerializer):
#     def validate(self, attrs):
#         data = super(CustomTokenRefreshSerializer, self).validate(attrs)
#         decoded_payload = token_backend.decode(data["access"], verify=True)

#         user = self.user
#         user.id = decoded_payload["user_id"]
#         # add filter query
#         data.update({"is_admin": user.is_admin})
#         return data
