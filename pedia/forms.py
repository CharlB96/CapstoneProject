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

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            if self.instance and self.instance.pk:
                self.fields['image'].initial = self.instance.image.url
                self.fields['image'].required = False
            else:
                self.fields['image'].required = True   
                self.fields['image'].initial = 'default_image_url'
