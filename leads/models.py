from django.db import models
from agents.models import Agent


class Lead(models.Model):
    frist_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    phoned = models.BooleanField(default=False)
    source = models.CharField(
        max_length=100,
        choices=[
            ("YT", "youtube"),
            ("Google", "Google"),
            ("NewsLetter", "NewsLetter"),
        ],
    )
    profile_image = models.ImageField(blank=True, null=True)
    special_files = models.FileField(blank=True, null=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
