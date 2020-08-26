from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Game, Team, Competition
from .serializers import GamesSerializer, TeamSerializer, CompetitionSerializer
# Create your views here.


class GamesView(ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GamesSerializer


class TeamView(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class CompetitionView(ModelViewSet):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
