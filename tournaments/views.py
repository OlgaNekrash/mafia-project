from django.shortcuts import render, get_object_or_404, redirect
from .models import Tournament, Participant
from .forms import ParticipantForm
from django.contrib import messages


def tournament_list(request):
    tournaments = Tournament.objects.all()
    return render(request, 'tournaments/tournament_list.html', {'tournaments': tournaments})


def tournament_detail(request, pk):
    tournament = get_object_or_404(Tournament, pk=pk)
    participants = Participant.objects.filter(tournament=tournament)

    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            participant = form.save(commit=False)
            participant.tournament = tournament

            participant.save()
            messages.success(request, 'Вы успешно зарегистрировались на турнир!')

            with open('participants.txt', 'a', encoding='utf-8') as file:
                file.write(
                    f'{participant.full_name} - {participant.nickname} - {participant.age} - '
                    f'{participant.experience} лет опыта - {participant.phone_number} - {participant.tg_link}\n'
                )

            return redirect('tournament_detail', pk=tournament.pk)
    else:
        form = ParticipantForm()

    return render(request, 'tournaments/tournament_detail.html', {
        'tournament': tournament,
        'participants': participants,
        'form': form
    })
