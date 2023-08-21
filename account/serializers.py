from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User


class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    first_name = serializers.CharField(required=True)
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["email", "username", "first_name", "password", "password2"]
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
        )
        # password = validated_data.pop('password', None)
        # instance = self.Meta.model(**validated_data)
        # if password is not None:
        #     instance.set_password(password)
        user.set_password(validated_data["password"])
        user.save()
        return user
