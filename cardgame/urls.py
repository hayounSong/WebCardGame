from unicodedata import name
from django.urls import path
from . import views

app_name='cardgame'
urlpatterns = [
    path('', views.main, name='main'),
    path('list_game/', views.list_game, name='list_game'),
    path('<int:pk>/delete_game/', views.delete_game, name='delete_game'),
    path('user_ranking/', views.user_ranking, name='user_ranking'),
    path('<int:pk>/detail_game/',views.detail_game,name='detail_game')
]