from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import AddArticleForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def article_view(request):
    """ 
    View to display articles
    """
    query = request.GET.get('q')

    if query:
        article_items = Article.objects.filter(
            Q(animal_name__icontains=query) | 
            Q(binomial_name__icontains=query) |
            Q(location__icontains=query) |
            Q(diet__icontains=query) |
            Q(description__icontains=query),
            approved=True
        )
        
        if not article_items.exists():
            messages.warning(request, 'No results found for the search query.')
            
    else:
        article_items = Article.objects.filter(approved=True)

    items_per_page = 8
    paginator = Paginator(article_items, items_per_page)
    page = request.GET.get('page')

    try:
        article_items = paginator.page(page)
    except PageNotAnInteger:
        article_items = paginator.page(1)
    except EmptyPage:
        article_items = paginator.page(paginator.num_pages)

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

    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to add an article.')
        return redirect('article_view')

    if request.method == "POST":
        article_form = AddArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.user = request.user
            article.save()
            messages.success(request, 'Article submitted and awaiting approval')
            return redirect('article_view')
        else:
            messages.error(request, 'Error adding article')

    else:
        article_form = AddArticleForm()

    return render(request, 'pedia/add_article.html', {'article_form': article_form})


def edit_article(request, article_id=None):
    """
    View to add or edit an article
    """
    if not request.user.is_authenticated:
        messages.error(request, 'You must be at least an admin to edit an article.')
        return redirect('login')

    article = get_object_or_404(Article, id=article_id) if article_id else Article()

    if article.user != request.user and not request.user.is_staff:
        messages.error(request, 'You do not have permission to edit this article.')
        return redirect('article_view')

    article_form = AddArticleForm(request.POST or None, request.FILES or None, instance=article)

    if request.method == "POST":
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.user = request.user
            article.save()
            messages.success(request, 'Article updated successfully')
            return redirect('article_detail', article_id=article.id)
        else:
            messages.error(request, 'Error updating article')

    return render(request, 'pedia/add_article.html', {'article_form': article_form})



def delete_article(request, article_id=None):
    """
    View for deleting articles
    """
    if not request.user.is_authenticated:
        messages.error(request, 'You must be at least an admin to delete an article.')
        return redirect('login')

    if article_id:
        article = get_object_or_404(Article, id=article_id)
        if article.user != request.user:
            messages.error(request, 'You do not have permission to edit this article.')
            return redirect('article_view')
        else:
            article_form = AddArticleForm(request.POST or None, request.FILES or None, instance=article)
    else:
        article = Article()
        article_form = AddArticleForm(request.POST or None, request.FILES or None, instance=article)

    if article.user == request.user:
        article.delete()
        messages.success(request, 'Article deleted.')
    else:
        messages.error(request, 'You can only delete your own article.')

    return redirect('article_view')