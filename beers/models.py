from django.db import models

# Create your models here.
from django.db import models


class Beer(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=2000)
    
    def __str__(self) -> str:
        return f'{self.id.__str__()}. {self.title}'