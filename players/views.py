from django.shortcuts import render, get_object_or_404
from .models import Players


def players_list(request):
    search_query = request.GET.get('search', '')
    players = Players.objects.all()

    if search_query:
        players = players.filter(nickname__icontains=search_query)

    sort_by = request.GET.get('sort', '')
    if sort_by == 'alphabetical':
        players = players.order_by('nickname')

    return render(request, 'players/players_list.html', {'players': players})


def player_detail(request, pk):
    player = get_object_or_404(Players, pk=pk)
    clubs = player.clubs.all()

    return render(request, 'players/player_detail.html', {
        'player': player,
        'clubs': clubs,
    })
