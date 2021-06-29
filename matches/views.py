from django.shortcuts import render, redirect

# Create your views here.
from matches.forms import MatchForm


def create_match(request):
    form = MatchForm()
    if request.method == "POST":
        form = MatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            form = MatchForm(request.POST)

    return render(request, "matches/matches.html", {"form": form})
