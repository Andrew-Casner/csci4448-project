from django.shortcuts import render
from manager.main import Runner
# Create your views here.
r = Runner()
def index(request):
    turny = r.getTourny()
    return render(request, "index.html", {'turny': turny})

def teams(request):

    teams = r.getTeams()
    return render(request, "teams.html", {'teams': teams})

def players(request):
    players = r.getPlayers()
    return render(request, "players.html", {'players': players})

def tournament(request):
    turny = r.getTourny()
    return render(request, "tournament.html", {'turny': turny})

def login(request):
    return render(request, "login.html")
