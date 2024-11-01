from django import forms
from .models import Players


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Players
        fields = ['nickname', 'experience', 'photo', 'clubs', 'tournaments']
