from django.urls import path 
from .views import Index, LoggedInHome, HomeRedirectView

urlpatterns = [
    path('', Index.as_view(), name='home_logged_out'),
    path('logged-in-home/', LoggedInHome.as_view(), name='logged_in_home'),
    path('home-redirect/', HomeRedirectView.as_view(), name='home_redirect'),
]