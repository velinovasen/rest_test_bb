from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Game
from .serializers import GamesSerializer, CreateUserSerializer
# Create your views here.


class GamesView(APIView):

    def get(self, request):
        queryset = Game.objects.all()
        serializer_class = GamesSerializer(queryset, many=True)
        return Response(serializer_class.data)

    def push(self, request):
        pass


class CreateUserView(APIView):

    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
