from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def list_game(request):
    print(request.user.username)
    if request.user.is_authenticated:
        print('user is authenticated')
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
            # 'result' : result,
        }
        return render(request, 'list_game.html', context=ctx)

def delete_game(request, pk):
    game = CardGame.objects.get(id = pk)
    game.delete()
    return redirect('cardgame:list_game')


def user_ranking(request):
    users = User.objects.all().order_by('-point')
    ctx = {
        'users' : users
    }
    return render(request, 'user_ranking.html', context= ctx)
