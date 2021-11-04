from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/beers/<int:beer_id>/', views.api_beer),
]