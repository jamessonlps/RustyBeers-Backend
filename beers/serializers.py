from rest_framework import serializers
from .models import User, BeersFavoritesCounter


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'lastname', 'email', 'password', 'favorites']

class BeersFavoritesCounter(serializers.ModelSerializer):
    class Meta:
        model = BeersFavoritesCounter
        fields = ['beer_id', 'counter']