# Generated by Django 4.2.4 on 2023-08-18 11:46

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("email", models.EmailField(max_length=100, unique=True)),
                ("username", models.CharField(max_length=50, unique=True)),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "profile_pic",
                    models.ImageField(blank=True, null=True, upload_to="img/account"),
                ),
                (
                    "bio",
                    models.TextField(
                        blank=True, default="", max_length=2000, null=True
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(auto_now_add=True, verbose_name="date joined"),
                ),
                (
                    "last_login",
                    models.DateTimeField(auto_now_add=True, verbose_name="last login"),
                ),
                ("is_active", models.BooleanField(default=True)),
                (
                    "is_customer",
                    models.BooleanField(default=True, verbose_name="Customer"),
                ),
                (
                    "is_artist",
                    models.BooleanField(default=False, verbose_name="Artist"),
                ),
                ("is_staff", models.BooleanField(default=False)),
                ("is_admin", models.BooleanField(default=False)),
                ("is_superuser", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
