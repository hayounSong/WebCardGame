from django.urls import path
from django.urls import path, include
from . import views

app_name = 'cardgame'

urlpatterns = [
    path('<int:pk>/defense/', views.game_defense, name='game_defense'),
    path('', views.main, name='main'),
    path('list_game/', views.list_game, name='list_game'),
    path('<int:pk>/delete_game/', views.delete_game, name='delete_game'),
    path('user_ranking/', views.user_ranking, name='user_ranking'),
    path('attack_game/', views.attack_game, name='attack_game'),
    path('<int:pk>/detail_game/',views.detail_game,name='detail_game'),
    path('accounts/profile/',views.profile,name="profile")
]
