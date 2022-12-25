import uuid

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    username = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=200, blank=True)
    short_intro = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(
        blank=True, upload_to="profiles/", default="user-default.png"
    )
    social_github = models.CharField(max_length=200, blank=True)
    social_stackoverflow = models.CharField(max_length=200, blank=True)
    social_twitter = models.CharField(max_length=200, blank=True)
    social_linkedin = models.CharField(max_length=200, blank=True)
    social_youtube = models.CharField(max_length=200, blank=True)
    social_website = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return str(self.user.username)


class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return self.name
