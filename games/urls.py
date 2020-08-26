from django.urls import re_path, path, include
from rest_framework import routers
from games import views

router = routers.SimpleRouter()
router.register(r'games', views.GamesView, basename='games')
router.register(r'teams', views.TeamView, basename='teams')
router.register(r'competitions', views.CompetitionView, basename='competitions')

urlpatterns = [
    re_path('rest-auth/', include('rest_auth.urls')),
]

urlpatterns += router.urls
