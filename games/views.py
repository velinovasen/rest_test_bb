from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from .models import Game, Team, Competition
from .serializers import GamesSerializer, TeamSerializer, CompetitionSerializer, CreateUserSerializer
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


class CreateUserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer