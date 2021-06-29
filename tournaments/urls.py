from django.urls import path

from tournaments.views import create_tournament

urlpatterns = [
    path("create/", create_tournament, name="create_tournament"),
]
