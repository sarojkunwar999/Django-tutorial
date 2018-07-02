from django.http import Http404
from .models import Album
from django.shortcuts import render


#working with templates

def index(request):
    all_albums = Album.objects.all()

    context = {'all_albums': all_albums}
    return render(request, 'music/index.html', context)


def detail(request, album_id):
    try:
       album=Album.objects.get(id=album_id)
    except Album.DoesNotExist:
       raise Http404("Album doesnot exist!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    return render(request, 'music/detail.html', {'album': album})



