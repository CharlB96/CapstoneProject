from django.shortcuts import render
from django.contrib import messages
from django.views.generic import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Suggestion
from .forms import SuggestionForm

class AddSuggestion(LoginRequiredMixin, CreateView):
    """ Add suggestion view """
    template_name = "suggestion/suggestion.html"
    model = Suggestion
    form_class = SuggestionForm
    success_url = '/suggestion/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Your suggestion has been sent')
        return super(AddSuggestion, self).form_valid(form)
