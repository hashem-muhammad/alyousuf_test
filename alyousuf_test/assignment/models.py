from django.db import models
from django.contrib.auth.models import AbstractUser
from assignment.Manager.UserManager import UserManager


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    username = None
    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self) -> str:
        return f'{self.email}'


class PostType(models.Model):
    id = models.AutoField(primary_key=True)
    ptype = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.ptype}'


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey(PostType, on_delete=models.CASCADE, null=True)
    image = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=255, null=True)
    details = models.CharField(max_length=255)
    posted_date = models.DateField(auto_created=True, null=True)

    def __str__(self) -> str:
        return f'{self.title}'
