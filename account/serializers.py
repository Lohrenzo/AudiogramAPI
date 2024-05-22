from django.contrib.auth.password_validation import validate_password
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User


# class UserRegistrationSerializer(serializers.Serializer):
class UserListenerSerializer(UserCreateSerializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    first_name = serializers.CharField(max_length=255, required=True)
    last_name = serializers.CharField(required=False, max_length=255)
    password = serializers.CharField(
        write_only=True,
        max_length=105,
        required=True,
        validators=[validate_password],
    )
    password2 = serializers.CharField(
        write_only=True,
        max_length=105,
        required=True,
    )
    is_admin = serializers.BooleanField(default=False, read_only=True)
    is_listener = serializers.BooleanField(default=True, read_only=True)

    class Meta:
        model = User
        fields = [
            "email",
            "username",
            "first_name",
            "last_name",
            "password",
            "password2",
            "is_admin",
            "is_listener",
        ]
        # extra_kwargs = {
        #     # "password": {"write_only": True},
        #     'first_name': {'required': True},
        # }

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."},
            )
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
            is_listener=True,
        )
        # password = validated_data.pop('password', None)
        # instance = self.Meta.model(**validated_data)
        # if password is not None:
        #     instance.set_password(password)
        user.set_password(validated_data["password"])
        user.save()
        return user


class UserArtistSerializer(UserCreateSerializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=False)
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )
    password2 = serializers.CharField(write_only=True, required=True)
    is_admin = serializers.BooleanField(default=False, read_only=True)
    is_artist = serializers.BooleanField(default=True, read_only=True)
    is_listener = serializers.BooleanField(default=False, read_only=True)

    class Meta:
        model = User
        fields = [
            "email",
            "username",
            "first_name",
            "last_name",
            "password",
            "password2",
            "is_admin",
            "is_artist",
            "is_listener",
        ]
        # extra_kwargs = {
        #     # "password": {"write_only": True},
        #     'first_name': {'required': True},
        # }

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."},
            )
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data.get("last_name", ""),
            is_artist=True,
        )
        # password = validated_data.pop('password', None)
        # instance = self.Meta.model(**validated_data)
        # if password is not None:
        #     instance.set_password(password)
        user.set_password(validated_data["password"])
        user.save()
        return user
