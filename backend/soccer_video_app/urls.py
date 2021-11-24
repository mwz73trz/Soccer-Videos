from django.urls import path
from soccer_video_app import views

urlpatterns = [
    path('games/', views.get_games, name="get_games"),
]