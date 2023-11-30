from django.urls import path 
from .views import Article

urlpatterns = [
    path('', Article.as_view(), name='pedia')
]