from django import forms
from .models import *

class AttackForm(forms.Form):
    attack_num = forms.ModelChoiceField(queryset=Card.objects.all())
    defense_user = forms.ModelChoiceField(queryset=User.objects.all())
