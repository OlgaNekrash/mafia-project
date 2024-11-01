from django import forms
from .models import Participant


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['full_name', 'nickname', 'age', 'experience', 'phone_number', 'tg_link']

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 18 or age > 90:
            raise forms.ValidationError('Возраст должен быть от 18 до 90 лет.')
        return age

    def clean_experience(self):
        experience = self.cleaned_data.get('experience')
        if experience is None:
            raise forms.ValidationError('Опыт должен быть указан.')
        if experience < 0.5 or experience > 40:
            raise forms.ValidationError('Опыт должен быть от 0.5 до 40 лет.')
        return experience

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        if not all(c.isalpha() or c.isspace() for c in full_name):
            raise forms.ValidationError('В полном имени могут быть только буквы и пробелы.')
        return full_name
