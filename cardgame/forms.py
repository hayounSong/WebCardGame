from django import forms
from .models import *

class DefenseForm(forms.Form):
    defense_num = forms.ModelChoiceField(
        queryset = Card.objects.order_by('?')[:5]
    )
