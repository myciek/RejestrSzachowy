from django.forms import ModelForm, CharField, DateField
from datetime import date
from tournaments.models import Tournament


class TournamentForm(ModelForm):
    name = CharField(max_length=512, label="Nazwa")
    date = DateField(label="Data", initial=date.today())

    class Meta:
        model = Tournament
        fields = ("name", "date", "arbiter")
