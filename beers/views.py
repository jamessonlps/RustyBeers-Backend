from django.http.response import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BeersFavoritesCounter, User
from .serializers import UserSerializer


@api_view(['POST'])
def api_loggin_user(request):
    """
        Recebe request com email e senha e valida no banco de dados.
        Se autorizado, retorna os dados completos do usuário.
    """
    user_email    = request.data.get('email')
    user_password = request.data.get('password')
    try:
        user = User.objects.get(email=user_email)
    except User.DoesNotExist:
        return HttpResponse("user does not exist")

    if (user_password == user.password):
        user_serialized = UserSerializer(user)
        return Response(user_serialized.data)
    else:
        return HttpResponse("incorrect password")


@api_view(['POST'])
def api_register_user(request):
    """
        Recebe request com dados de cadastro e cria usuário no banco
        de dados.
    """
    user_name     = request.data.get('name')
    user_lastname = request.data.get('lastname')
    user_email    = request.data.get('email')
    user_password = request.data.get('password')

    try:
        new_user = User(
            name=user_name,
            lastname=user_lastname,
            email=user_email,
            password=user_password,
            favorites=[]
        )
        new_user.save()
        
        new_user_serialized = UserSerializer(new_user)
        return Response(new_user_serialized.data)
    except User.DoesNotExist:
        return HttpResponse('user already exists')


@api_view(['POST'])
def api_add_favorite(request):
    """
        Recebe o id de uma bebida que deve ser adicionada à
        lista de favoritos do usuário identificado pelo email.
    """
    user_email = request.data.get('email')
    beer_id    = request.data.get('beer_id')

    # Se a bebida ainda não teve um voto, registra ela para
    # começar a sua contagem
    try:
        beer = BeersFavoritesCounter.objects.get(beer_id=beer_id)
    except BeersFavoritesCounter.DoesNotExist:
        beer = BeersFavoritesCounter(beer_id=beer_id, counter=1)

    try:
        user = User.objects.get(email=user_email)
        if beer_id not in user.favorites:
            user.favorites.append(beer_id)
            beer.save()
            user.save()
            return HttpResponse('Drink successfully added to favorites')
        else:
            return HttpResponse('This drink is already in favorites')
    except Exception as e:
        return HttpResponse(e)


@api_view(['POST'])
def api_remove_from_favorites(request):
    """
        Remove bebida da lista de favoritos do usuário
    """
    user_email = request.data.get('email')
    beer_id    = request.data.get('beer_id')
    try:
        user = User.objects.get(email=user_email)
        beer = BeersFavoritesCounter.objects.get(beer_id=beer_id)

        user.favorites.remove(beer_id)
        beer.counter -= 1

        user.save()
        beer.save()
        
        resp = {'favorites': user.favorites}
        return Response(resp)
    except:
        return HttpResponse('failure')


@api_view(['POST'])
def api_get_favorites(request):
    """
        Retorna os ids das bebidas favoritas de um usuário.
    """
    user_email = request.data.get('email')
    try:
        user = User.objects.get(email=user_email)
        resp = {'favorites': user.favorites}
        return Response(resp)
    except Exception as e:
        return HttpResponse(e)