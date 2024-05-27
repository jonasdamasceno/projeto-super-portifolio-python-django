from django.core.exceptions import ValidationError


def validate_profile_fields(value):

    MIN_LENGTH = 1
    MAX_LENGTH = 500

    if len(value) <= MIN_LENGTH:
        raise ValidationError(
            f"Value cannot be empty or less than {MIN_LENGTH} characters."
        )
    elif len(value) > MAX_LENGTH:
        raise ValidationError(f"Value cannot exceed {MAX_LENGTH} characters.")
