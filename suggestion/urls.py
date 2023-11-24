from django.urls import path
from .views import AddSuggestion


urlpatterns = [
    path('', AddSuggestion.as_view(), name="suggestion")
]