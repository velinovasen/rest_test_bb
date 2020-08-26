from django.urls import re_path, path, include
from rest_framework import routers
from games import views

router = routers.SimpleRouter()
router.register(r'games', views.GamesView)
router.register(r'teams', views.TeamView)
router.register(r'competitions', views.CompetitionView)
router.register(r'register', views.CreateUserView)

urlpatterns = [
    re_path('rest-auth/', include('rest_auth.urls')),

]

urlpatterns += router.urls
