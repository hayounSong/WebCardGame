from django import forms
from .models import *


class AttackForm(forms.Form):
    attack_num = forms.ModelChoiceField(
        queryset=Card.objects.order_by('?')[:5])
    defense_user = forms.ModelChoiceField(queryset=User.objects.all())
