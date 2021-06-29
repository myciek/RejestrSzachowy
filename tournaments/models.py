from django.db import models
from datetime import date

# Create your models here.
from users.models import User


class Tournament(models.Model):
    arbiter = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={"is_arbiter": True})
    date = models.DateField(default=date.today)
    name = models.TextField(max_length=512)

    def __str__(self):
        return self.name
