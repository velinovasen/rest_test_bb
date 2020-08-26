from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Game, Team, Competition


class GamesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ["team_home", "team_away", "competition", "home_odd",
                  "draw_odd", "away_odd", "prediction", "result", "won", "profit"]


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ["name", "country", "continent"]


class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Competition
        fields = ["name", "continent", "type"]



# class CreateUserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ["id", "username", "password", "email", "first_name", "last_name"]
#         write_only_fields = ["password",]
#         read_only_fields = ["id",]
#         extra_kwargs = {'password': {'write_only': True}}              # HIDES PASSWORD FROM GET, AFTER THE POST METHOD
#
#     def create(self, validated_data):
#         user = User.objects.create(
#             username=validated_data["username"],
#             email=validated_data["email"],
#             first_name=validated_data["first_name"],
#             last_name=validated_data["last_name"]
#         )
#
#         user.set_password(validated_data["password"])
#         user.save()
#         return user