from django.db import models
from django.core.validators import URLValidator  # Import built-in URLValidator
from projects.validators import (
    validate_profile_fields,
)  # Optional custom validator


class Profile(models.Model):
    name = models.CharField(
        max_length=100, validators=[validate_profile_fields]
    )
    github = models.URLField(
        validators=[URLValidator, validate_profile_fields]
    )  # Apply both validators
    linkedin = models.URLField(
        validators=[URLValidator, validate_profile_fields]
    )  # Apply both validators
    bio = models.TextField(
        blank=True, validators=[validate_profile_fields]
    )  # Allow blank bios

    def __str__(self):
        return self.name
