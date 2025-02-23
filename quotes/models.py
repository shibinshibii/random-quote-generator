from django.db import models

# Create your models here.

class Quote(models.Model):
    content=models.TextField()
    author=models.TextField(max_length=100)

    def __str__(self):
        return f'"{self.content}"-{self.author}'
