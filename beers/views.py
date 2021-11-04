from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Beer
from .serializers import BeerSerializer



def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        # request para criar nota
        new_beer = Beer(title=title, content=content)
        if request.POST.__contains__('create'):
            new_beer.save()
        return redirect('index')
    else:
        all_beers = Beer.objects.all()
        return render(request, 'beers/index.html', {'beers': all_beers})

@api_view(['GET', 'POST'])
def api_beer(request, beer_id):
    try:
        beer = Beer.objects.get(id=beer_id)
    except Beer.DoesNotExist:
        raise Http404()

    if request.method == 'POST':
        new_beer_data = request.data
        beer.title = new_beer_data['title']
        beer.content = new_beer_data['content']
        beer.save()

    serialized_beer = BeerSerializer(beer)
    return Response(serialized_beer.data)