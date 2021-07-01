from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.
from matches.models import Match
from tournaments.forms import TournamentForm
from tournaments.models import Tournament


def create_tournament(request):
    form = TournamentForm()
    if request.method == "POST":
        form = TournamentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            form = TournamentForm(request.POST)

    return render(request, "tournaments/tournaments.html", {"form": form})


def tournament_details(request, pk):
    tournament = Tournament.objects.get(id=pk)
    matches = Match.objects.filter(tournament=tournament.id)
    context = {"tournament":
                   {"name": tournament.name,
                    "matches": matches}}
    return render(request, "tournaments/matches_list.html", context)


def tournament_list(request):
    tournaments = []
    if request.user.is_arbiter:
        tournaments = Tournament.objects.filter(arbiter=request.user)
    else:
        for match in request.user.matches_white.all():
            tournaments.append(match.tournament)
        for match in request.user.matches_black.all():
            tournaments.append(match.tournament)
        tournaments = set(tournaments)

    context = {"tournaments": tournaments}
    return render(request, "tournaments/tournaments_list.html", context)
