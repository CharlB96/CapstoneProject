from .models import Article
from django import forms

class AddArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = (
            'image', 'image_alt', 'animal_name', 'binomial_name',
            'location', 'diet', 'description', 'map', 'map_alt'
            )
        labels = {
            'animal_name': 'Animal Name',
            'binomial_name': 'Binomial Name',
            'image': 'Add image',
            'image_alt': 'Describe the image briefly',
            'location': 'Location',
            'diet': 'Diet',
            'description': 'Description of animal',
            'map': 'Add map of location',
            'map_alt': 'Describe map briefly'
        }