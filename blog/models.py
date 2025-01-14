from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):        #each class is a table and each variable here is field
    title=models.CharField(max_length=100) 
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User, on_delete=models.CASCADE)   #if a user is deleted-> delete its post and not the other way around.

    def __str__(self):
        return self.title