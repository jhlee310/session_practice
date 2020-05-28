from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField(null=True)
    deadline = models.DateTimeField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
  

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')