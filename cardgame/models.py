from random import choice
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    point = models.IntegerField(default=0)


class Card(models.Model):
    card_num = models.IntegerField()

    def __str__(self):
        return str(self.card_num)


class Attack(models.Model):
    attack_user = models.ForeignKey(User, on_delete=models.CASCADE)
    num = models.ForeignKey(Card, on_delete=models.CASCADE)


class Defense(models.Model):
    defense_user = models.ForeignKey(User, on_delete=models.CASCADE)
    num = models.ForeignKey(Card, on_delete=models.CASCADE, null=True, blank=True)


MODE_CHOICE = {('큰 수', '큰 수'),('작은 수', '작은 수')}
STATUS_CHOICE = {('진행중', '진행중'),('끝', '끝')}
class CardGame(models.Model):
    mode = models.CharField(max_length=20, choices=MODE_CHOICE) ## 큰 수가 이기는 게임 or 작은 수가 이기는 게임 (랜덤)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE) ## 진행중(attack, defense 다 있는데, defense.num은 NULL) or 끝난거 (denfense.num이 값을 가짐)
    attack = models.OneToOneField(Attack, on_delete=models.CASCADE)
    defense = models.OneToOneField(Defense, on_delete=models.CASCADE)
    victory_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    