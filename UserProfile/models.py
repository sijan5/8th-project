from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    interests = models.TextField(blank=True)
    learning_history = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
