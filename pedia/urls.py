from django.urls import path 
from .views import article_view, article_detail, add_article, edit_article, delete_article

urlpatterns = [
    path('', article_view, name='article_view'),
    path('<int:article_id>/', article_detail, name='article_detail'),
    path('add/', add_article, name='add_article'),
    path('edit_article/<int:article_id>/', edit_article, name='edit_article'),
    path('delete_article/<int:article_id>/', delete_article, name='delete_article'),
]