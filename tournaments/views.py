from django.shortcuts import render, redirect

# Create your views here.
from tournaments.forms import TournamentForm


def create_tournament(request):
    form = TournamentForm()
    if request.method == "POST":
        form = TournamentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            form = TournamentForm()

    return render(request, "tournaments/tournaments.html", {"form": form})
