import os

from django.core.exceptions import ValidationError
from PIL import Image


def validate_cover_image_size(image):
    if image:
        max_width = 500
        max_height = 500
        new_img = Image.open(image)

        if new_img.width > max_width or new_img.height > max_height:
            new_img.thumbnail((max_width, max_height))
            new_img.save(image.path)


def validate_image_file_extension(value):
    extension = os.path.splitext(value.name)[1]
    valid_extensions = [".jpg", ".jpeg", ".png", ".gif"]
    if not extension.lower() in valid_extensions:
        raise ValidationError("Unsupported file extension")
