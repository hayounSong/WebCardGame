from django.shortcuts import render, redirect, get_object_or_404
from cardgame.forms import DefenseForm
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


def game_win(attack, defense, pk, game):
    
    if game.mode == '큰 수':
        if attack.num.card_num >= defense.num.card_num:
            victory_user = attack.attack_user 
            attack.attack_user.point += attack.num.card_num
            defense.defense_user.point -= defense.num.card_num
        
        else:
            victory_user = defense.defense_user
            attack.attack_user.point -= attack.num.card_num
            defense.defense_user.point += defense.num.card_num

    else:
        if attack.num.card_num <= defense.num.card_num:
            victory_user = attack.attack_user
            attack.attack_user.point += attack.num.card_num
            defense.defense_user.point -= defense.num.card_num

        else:
            victory_user = defense.defense_user
            attack.attack_user.point -= attack.num.card_num
            defense.defense_user.point += defense.num.card_num

    game.attack.attack_user.save()
    game.defense.defense_user.save()

    return [victory_user, attack.attack_user.point, defense.defense_user.point]

    
def game_defense(request, pk):
    game = CardGame.objects.get(id = pk) 

    if request.method == 'POST':
        defense = game.defense
        defense.num = Card.objects.get(id = request.POST['defense_num'])
        defense.save()

        attack = game.attack
        game.status = '끝'
        game.defense = defense
        game.victory_user, game.attack.attack_user.point, game.defense.defense_user.point = game_win(attack, defense, pk, game)
        print(game.victory_user, game.attack.attack_user.point, game.defense.defense_user.point)
        game.save()

        return redirect('cardgame:game_defense', game.pk)  # 반격하기 누르면 게임정보 띄워준다. game_detail로 바꾸기.
    
    else:
        form = DefenseForm()
        ctx = {
            'form': form,
            'attack': game.attack.attack_user.username,
        }
        return render(request, 'defense_form.html', context = ctx)