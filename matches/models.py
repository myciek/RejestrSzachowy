from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
from tournaments.models import Tournament
from users.models import User

RESULTS = (
    (1, _("Biale")),
    (2, _("Remis")),
    (3, _("Czarne"))
)


class Match(models.Model):
    white = models.ForeignKey(User, on_delete=models.CASCADE, related_name="matches_white")
    black = models.ForeignKey(User, on_delete=models.CASCADE, related_name="matches_black")
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name="matches")
    result = models.IntegerField(choices=RESULTS)

    def __str__(self):
        return f"{self.white.last_name} vs {self.black.last_name}"
