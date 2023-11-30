from django.shortcuts import render
from django.views.generic import TemplateView


class Article(TemplateView):
    template_name = 'pedia/pedia.html'