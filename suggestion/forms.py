from django import forms

from .models import Suggestion


class SuggestionForm(forms.ModelForm):
    """ Form to make suggestion """
    class Meta:
        model = Suggestion
        fields = ['animal_name', 'description']

        labels = {
            'animal_name': 'Name your animal',
            'description': 'Why should we include it?',
        }
