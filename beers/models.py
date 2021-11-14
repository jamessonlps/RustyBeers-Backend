from django.db import models
from django.contrib.postgres.fields import ArrayField

class User(models.Model):
    name      = models.CharField(max_length=32)
    lastname  = models.CharField(max_length=32)
    email     = models.EmailField(unique=True, max_length=32)
    password  = models.CharField(max_length=32)
    favorites = ArrayField(models.IntegerField(), blank=True)

    def __str__(self) -> str:
        return f"{self.email}. {self.name} {self.lastname}"


class BeersFavoritesCounter(models.Model):
    beer_id = models.IntegerField(primary_key=True, unique=True)
    counter = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.beer_id}. {self.counter} votes'