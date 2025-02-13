# Generated by Django 4.2.3 on 2024-05-28 12:48

from django.db import migrations, models
import django.db.models.deletion
import projects.validators


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        validators=[
                            projects.validators.validate_profile_fields
                        ],
                    ),
                ),
                (
                    "github",
                    models.URLField(
                        validators=[
                            projects.validators.validate_profile_fields
                        ]
                    ),
                ),
                (
                    "linkedin",
                    models.URLField(
                        validators=[
                            projects.validators.validate_profile_fields
                        ]
                    ),
                ),
                (
                    "bio",
                    models.TextField(
                        validators=[
                            projects.validators.validate_profile_fields
                        ]
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Project",
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
                (
                    "name",
                    models.CharField(
                        max_length=50,
                        validators=[
                            projects.validators.validate_profile_fields
                        ],
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        max_length=500,
                        validators=[
                            projects.validators.validate_profile_fields
                        ],
                    ),
                ),
                (
                    "github_url",
                    models.URLField(
                        validators=[
                            projects.validators.validate_profile_fields
                        ]
                    ),
                ),
                (
                    "keyword",
                    models.CharField(
                        max_length=50,
                        validators=[
                            projects.validators.validate_profile_fields
                        ],
                    ),
                ),
                (
                    "key_skill",
                    models.CharField(
                        max_length=50,
                        validators=[
                            projects.validators.validate_profile_fields
                        ],
                    ),
                ),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="projects",
                        to="projects.profile",
                    ),
                ),
            ],
        ),
    ]
