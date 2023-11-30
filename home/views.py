from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, RedirectView
from django.urls import reverse_lazy


class Index(TemplateView):
    template_name = 'home/index.html'

class LoggedInHome(LoginRequiredMixin, TemplateView):
    template_name= 'home/logged-in-home.html'
    login_url = reverse_lazy('home_logged_out')

class HomeRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return reverse_lazy('logged_in_home')
        else:
            return reverse_lazy('home_logged_out')