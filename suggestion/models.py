from django.db import models
from django.contrib.auth.models import User


class Suggest(models.Model):
    """
    A model for users to submit suggestions for animals to include on the site
    """
    user = models.ForeignKey(User, related_name="suggester", on_delete=models.CASCADE)
    animal_name = models.CharField(max_length=30, null=False, blank=False)
    description = models.TextField(max_length=200, null=False, blank=False)
    post_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['post_date']

    def __str__(self):
        return str(self.animal_name)
