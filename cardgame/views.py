from django.shortcuts import render, redirect, get_object_or_404
from cardgame.forms import DefenseForm
from django.shortcuts import render, redirect, get_object_or_404

from django.shortcuts import render, redirect
from .models import *
from .form import *
import random


# Create your views here.


def main(request):
    user = request.user
    ctx = {
        'user': user
    }
    return render(request, 'main.html', ctx)


def list_game(request):
    if request.user.is_authenticated:
        # 현재 로그인한 유저가 속하는 게임들
        end_attack_games = CardGame.objects.filter(
            attack__attack_user__username=request.user.username, status='끝')
        proceed_attack_games = CardGame.objects.filter(
            attack__attack_user__username=request.user.username, status='진행중')
        end_defense_games = CardGame.objects.filter(
            defense__defense_user__username=request.user.username, status='끝')
        proceed_defense_games = CardGame.objects.filter(
            defense__defense_user__username=request.user.username, status='진행중')

        end_games = end_attack_games.union(end_defense_games)
        proceed_games = proceed_attack_games.union(proceed_defense_games)

        ctx = {
            'end_games': end_games,
            'proceed_games': proceed_games,
            'current_user': request.user,
            'count' : 1,
        }
        return render(request, 'list_game.html', context=ctx)

def attack_game(request):
    if request.method == 'POST':
        game = CardGame()
        game.mode = random.choice(['큰 수', '작은 수'])
        game.status = '진행중'

        attack = Attack()
        attack.attack_user = User.objects.get(username=request.user)
        attack.num = Card.objects.get(id=request.POST['attack_num'])
        attack.save()

        defense = Defense()
        defense.defense_user = User.objects.get(
            id=request.POST['defense_user'])
        defense.save()

        game.attack = attack
        game.defense = defense
        game.save()

        return redirect('cardgame:list_game')

    else:
        form = AttackForm()
        form.fields['defense_user'].queryset = User.objects.exclude(
            id=request.user.id)
        return render(request, 'attack_form.html', locals())

def delete_game(request, pk):
    game = CardGame.objects.get(id=pk)
    game.delete()
    return redirect('cardgame:list_game')


def user_ranking(request):
    users = User.objects.all().order_by('-point')
    user_num = User.objects.count
    print(user_num)
    ctx = {
        'users': users,
        'user_num': user_num
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
        game.save()

        return redirect('cardgame:detail_game', game.pk)  # 반격하기 누르면 게임정보 띄워준다. game_detail로 바꾸기.
    
    else:
        form = DefenseForm()
        ctx = {
            'form': form,
            'attack': game.attack.attack_user.username,
        }
        return render(request, 'defense_form.html', context = ctx)

def detail_game(request,pk):
    game=get_object_or_404(CardGame,id=pk)
    
    if game.status=="끝":
        ctx={'game':game,
        'current_user':request.user
        }
        return render(request,template_name='detail_end.html',context=ctx)
    if game.status=="진행중":
        ctx={'game':game,
        'current_user':request.user
       }
        return render(request,template_name='detail_progress.html',context=ctx)


def profile(request):
    
    return redirect('cardgame:main')