from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Article(models.Model):
    """
    A model for superuser to create, read, update, and delete articles
    """
    user = models.ForeignKey(User, related_name="author", on_delete=models.CASCADE)
    image = CloudinaryField('image', default='placeholder')
    image_alt = models.CharField(max_length=50, null=False, blank=False, default="image")
    animal_name = models.CharField(max_length=50, null=False, blank=False)
    binomial_name = models.CharField(max_length=50, null=False, blank=False, default="(Genus) (Species)")
    location = models.CharField(max_length=50, null=False, blank=False)
    diet = models.CharField(max_length=30, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    post_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['post_date']

    def __str__(self):
        return str(self.animal_name)
