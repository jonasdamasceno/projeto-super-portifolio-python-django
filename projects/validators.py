from django.core.exceptions import ValidationError


def validate_profile_fields(value):
    if not value or len(value) > 500 or len(value) == 0:
        raise ValidationError("Invalid Value")
