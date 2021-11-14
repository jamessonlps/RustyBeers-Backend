from django.contrib import admin
from .models import User, BeersFavoritesCounter

admin.site.register(User)
admin.site.register(BeersFavoritesCounter)