from django.urls import re_path, path, include

from games import views

urlpatterns = [
    re_path("all/", views.GamesView.as_view()),
    re_path('rest-auth/', include('rest_auth.urls')),
    re_path('register/', views.CreateUserView.as_view()),

]