from django.shortcuts import render
from .models import Album

# Create your views here.


def album_list(request):
    return render(request, 'album/album_list.html', {})
