from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Game
from .serializers import GamesSerializer
# Create your views here.


class GamesView(APIView):

    def get(self, request):
        queryset = Game.objects.all()
        serializer_class = GamesSerializer(queryset, many=True)
        return Response(serializer_class.data)

    def create(self, request):
        pass

    def push(self, request):
        pass
