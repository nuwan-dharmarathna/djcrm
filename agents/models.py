from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Agent(models.Model):
    frist_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return f"{self.frist_name} {self.last_name}"
