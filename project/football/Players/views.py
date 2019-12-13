from django.shortcuts import render
from .models import Player


def players(request):
    try:
        players = Player.objects.all()
        return render(request, 'players.html', {'players':players})
    except:
        return render(request, 'players.html')

def detail(request, pk):
    players = Player.objects.get(pk=pk)
    return render(request, 'playerdetails.html', {'players': players})

# Create your views here.
