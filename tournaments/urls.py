from django.urls import path

from tournaments.views import create_tournament, tournament_details, tournament_list

app_name = "tournaments"
urlpatterns = [
    path("create/", create_tournament, name="create_tournament"),
    path("<pk>/", tournament_details, name="tournament_details"),
    path("", tournament_list, name="tournament_list"),

]
