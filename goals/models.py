from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.


class Goal(models.Model):
    plan = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    deadline = models.DateField(default=date.today())
    created = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.author.username