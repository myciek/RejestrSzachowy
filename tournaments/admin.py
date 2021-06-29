from django.contrib import admin

# Register your models here.
from tournaments.models import Tournament

admin.site.register(Tournament)
