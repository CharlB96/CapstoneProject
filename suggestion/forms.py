from django import forms

from .models import Suggestion


class SuggestionForm(forms.ModelForm):
    """ Form to make suggestion """
    class Meta:
        model = Suggestion
        fields = ['user', 'animal_name', 'description']

        labels = {
            'user': 'Enter your username',
            'animal_name': 'Name your animal',
            'description': 'Why should we include it?',
        }