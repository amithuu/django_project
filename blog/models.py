from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Each class will be its own table in the database..

# creating a post field which is creating a attributes inside the table..

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # here we are using the reverse() that how to find the url for the any specific model.
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})
    
    #[difference b/w reverse and redirect]:
    # redirect: it just reditrectes the page to specific path mentioned.
    # reverse: it finds the url for the specific model, and return the full path of the location.
