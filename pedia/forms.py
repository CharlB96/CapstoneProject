from .models import Article
from django import forms

class AddArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = (
            'image', 'image_alt', 'animal_name', 'binomial_name',
            'location', 'diet', 'description', 'map', 'map_alt'
            )