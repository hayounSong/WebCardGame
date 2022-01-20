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
    attack_num = models.ForeignKey(Card, on_delete=models.CASCADE)


class Defense(models.Model):
    defense_user = models.ForeignKey(User, on_delete=models.CASCADE)
    dense_num = models.ForeignKey(Card, on_delete=models.CASCADE)


class CardGame(models.Model):
    mode = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    attack = models.ForeignKey(Attack, on_delete=models.CASCADE)
    defense = models.ForeignKey(Defense, blank=True, on_delete=models.CASCADE)

