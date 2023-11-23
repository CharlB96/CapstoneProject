from django.contrib import admin
from .models import Suggest

# Register your models here.

@admin.register(Suggest)
class SuggestAdmin(admin.ModelAdmin):
    list_display = (
        'animal_name',
        'description',
        'post_date',
    )