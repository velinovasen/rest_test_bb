from django.db import models

# Create your models here.

TYPES_OF_COMPETITIONS = [
    ("club", "club"),
    ("nation", "nation")
]

CONTINENTS = [
    ("EU", "Europe"),
    ("AS", "Asia"),
    ("AF", "Africa"),
    ("NA", "North America"),
    ("SA", "South America")
]


class Team(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    continent = models.CharField(max_length=100, choices=CONTINENTS)

    def __str__(self):
        return f"{self.name} - {self.country} - {self.continent}"


class Competition(models.Model):
    name = models.CharField(max_length=100)
    continent = models.CharField(max_length=20)
    type = models.CharField(max_length=20, choices=TYPES_OF_COMPETITIONS)

    def __str__(self):
        return f"{self.name} - {self.continent} - {self.type}"


class Game(models.Model):
    team_home = models.ForeignKey(Team, on_delete=models.CASCADE)
    team_away = models.ForeignKey(Team, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    home_odd = models.FloatField()
    draw_odd = models.FloatField()
    away_odd = models.FloatField()
    prediction = models.CharField(max_length=5)
    result = models.CharField(max_length=5, default="? - ?")
    won = models.BooleanField(default=False)
    profit = models.CharField(max_length=10, default=0)

    def __str__(self):
        return f"{self.team_home} - {self.result} - {self.team_away} - {self.won} {self.profit}"

