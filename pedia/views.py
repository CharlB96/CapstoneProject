from django.shortcuts import render
from .models import Article


def article_view(request):
    article_items = Article.objects.all()
    return render(request, 'pedia/pedia.html', {'article_items': article_items})