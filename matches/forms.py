from django.forms import ModelForm

from matches.models import Match


class MatchForm(ModelForm):

    class Meta:
        model = Match
        fields = ("white", "black", "tournament", "result")
