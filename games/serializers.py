from rest_framework.serializers import ModelSerializer
from .models import Game


class GamesSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = ["team_home", "team_away", "competition", "home_odd",
                  "draw_odd", "away_odd", "prediction", "result", "won", "profit"]
