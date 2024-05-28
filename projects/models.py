from django.db import models
from projects.validators import validate_profile_fields


class Profile(models.Model):
    name = models.CharField(
        max_length=100, validators=[validate_profile_fields]
    )
    github = models.URLField(validators=[validate_profile_fields])
    linkedin = models.URLField(validators=[validate_profile_fields])
    bio = models.TextField(validators=[validate_profile_fields])

    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    name = models.CharField(
        max_length=50, validators=[validate_profile_fields]
    )
    description = models.TextField(
        max_length=500, validators=[validate_profile_fields]
    )
    github_url = models.URLField(validators=[validate_profile_fields])
    keyword = models.CharField(
        max_length=50, validators=[validate_profile_fields]
    )
    key_skill = models.CharField(
        max_length=50, validators=[validate_profile_fields]
    )
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="projects"
    )

    def __str__(self) -> str:
        return self.name
