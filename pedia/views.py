from django.shortcuts import render, get_object_or_404
from .models import Article


def article_view(request):
    article_items = Article.objects.all()
    return render(request, 'pedia/pedia.html', {'article_items': article_items})

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'pedia/article_detail.html', {'article': article})