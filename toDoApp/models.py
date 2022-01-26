from django.db import models

class toDo(models.Model):
    title = models.TextField(max_length=200)
    is_done = models.BooleanField(default=False)    
    def __str__(self):
        return self.title