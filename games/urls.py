from django.urls import re_path, path

from games import views

urlpatterns = [
    re_path("", views.GamesView.as_view()),
]