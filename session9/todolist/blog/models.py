from django.db import models
from datetime import datetime

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField(null=True)
    deadline = models.DateTimeField(null=True)

# in the template. you should use
# {% if Todo.is_end_date %}
# {% elif %}
# {% endif %}    

    def __str__(self):
        return self.title
