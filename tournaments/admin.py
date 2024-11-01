from django.contrib import admin
from .models import Participant, Tournament


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'tournament')
