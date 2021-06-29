from django.urls import path

from matches.views import create_match

urlpatterns = [
    path("create/", create_match, name="create_match"),
]
