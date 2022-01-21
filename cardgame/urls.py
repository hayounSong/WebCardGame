from django.urls import path
from . import views

app_name = 'cardgame'

urlpatterns = [
    path('<int:pk>/defense/', views.game_defense, name='game_defense'),
]
