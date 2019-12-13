from django.shortcuts import render
from .models import Photo, Video


def gallery(request):
    photos = Photo.objects.all()
    return render(request, 'photos.html', {'photos':photos})


def videos(request):
    videos = Video.objects.all()
    return render(request, 'Videos.html', {'videos':videos})
# Create your views here.
