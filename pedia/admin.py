from django.contrib import admin
from .models import Article
# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'animal_name',
        'location',
        'diet',
        'description',
        'post_date',
    )