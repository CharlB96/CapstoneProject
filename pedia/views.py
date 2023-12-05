from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import AddArticleForm
from django.contrib import messages


def article_view(request):
    """ 
    View to display articles
    """
    article_items = Article.objects.filter(approved=True)
    return render(request, 'pedia/pedia.html', {'article_items': article_items})

def article_detail(request, article_id):
    """
    View to display the detailed page view
    """
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'pedia/article_detail.html', {'article': article})

def add_article(request):
    """
    View to add an article
    """
    if not request.user.is_authenticated:
        messages.error(request, 'You must be logged in to submit an article.')
        return redirect('login')

    if request.method == "POST":
        article_form = AddArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.user = request.user
            article.save()
            messages.success(request, 'Article submitted and awaiting approval')
            return redirect('article_view')
        else:
            messages.add_message(request, messages.ERROR, 'Error adding article')
    else:
        article_form = AddArticleForm()

    return render(request, 'pedia/add_article.html', {'article_form': article_form})