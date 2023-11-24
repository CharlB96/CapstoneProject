from django.contrib import admin
from .models import Suggestion

# Register your models here.

@admin.register(Suggestion)
class SuggestAdmin(admin.ModelAdmin):
    list_display = (
        'animal_name',
        'description',
        'post_date',
    )