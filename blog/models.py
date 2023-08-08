from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Each class will be its own table in the database..

# creating a post field which is creating a attributes inside the table..

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


