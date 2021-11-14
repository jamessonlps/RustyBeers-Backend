from django.urls import path

from . import views

urlpatterns = [
    path('api/auth/', views.api_loggin_user),
    path('api/auth/register/', views.api_register_user),
    path('api/add/favorite/', views.api_add_favorite),
    path('api/get/favorite/', views.api_get_favorites),
    path('api/remove/favorite/', views.api_remove_from_favorites)
]