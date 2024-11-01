from django.shortcuts import render, get_object_or_404

from tournaments.models import Tournament
from .models import Club
from blog.models import BlogPost


def club_list(request):
    clubs = Club.objects.all()
    return render(request, 'clubs/club_list.html', {'clubs': clubs})


def club_detail(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    tournaments = Tournament.objects.filter(club=club)
    players = club.players.all()
    blog_posts = BlogPost.objects.filter(clubs=club)  # Используем BlogPost
    return render(request, 'clubs/club_detail.html',
                  {'club': club, 'blog_posts': blog_posts, 'tournaments': tournaments, 'players': players})
