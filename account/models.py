from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class AccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            return ValueError("Users must have a username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            first_name=first_name,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    profile_pic = models.ImageField(
        upload_to="img/account",
        null=True,
        blank=True,
    )
    bio = models.TextField(max_length=2000, null=True, blank=True, default="")
    date_joined = models.DateTimeField(
        auto_now_add=True,
        verbose_name="date joined",
    )
    last_login = models.DateTimeField(
        auto_now_add=True,
        verbose_name="last login",
    )
    is_active = models.BooleanField(default=True)
    is_listener = models.BooleanField(
        verbose_name="Is Listener",
        default=False,
    )
    is_artist = models.BooleanField(
        verbose_name="Is Artist",
        default=False,
    )
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "first_name"]

    def __str__(self) -> str:
        return f"{self.username}"

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
