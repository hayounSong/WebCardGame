
from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def main(request):
    user = request.user
    ctx = {
        'user' : user
    }
    return render(request, 'main.html', ctx)


def list_game(request):
    if request.user.is_authenticated:
        # 현재 로그인한 유저가 속하는 게임들
        end_attack_games = CardGame.objects.filter(attack__attack_user__username = request.user.username, status='끝')
        proceed_attack_games = CardGame.objects.filter(attack__attack_user__username = request.user.username, status='진행중')
        end_defense_games = CardGame.objects.filter(defense__defense_user__username = request.user.username, status='끝')
        proceed_defense_games = CardGame.objects.filter(defense__defense_user__username = request.user.username, status='진행중')
        
        end_games = end_attack_games.union(end_defense_games)
        proceed_games = proceed_attack_games.union(proceed_defense_games)

        ctx = {
            'end_games' : end_games,
            'proceed_games' : proceed_games,
            'current_user' : request.user,
        }
        return render(request, 'list_game.html', context=ctx)

def delete_game(request, pk):
    game = CardGame.objects.get(id = pk)
    game.delete()
    return redirect('cardgame:list_game')


def user_ranking(request):
    users = User.objects.all().order_by('-point')
    user_num = User.objects.count
    print(user_num)
    ctx = {
        'users' : users,
        'user_num' : user_num
    }
    return render(request, 'user_ranking.html', context= ctx)