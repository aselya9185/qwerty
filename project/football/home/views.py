from django.shortcuts import render
from news.models import News
from photo.models import Video



def home(request):
    try:
        news = []
        videos=[]
        first = News.objects.get(pk=1)
        second = News.objects.get(pk=2)
        third = News.objects.get(pk=3)
        video1 = Video.objects.get(pk=1)
        video2 = Video.objects.get(pk=2)
        video3 = Video.objects.get(pk=3)
        videos.append(video1)
        videos.append(video2)
        videos.append(video3)
        news.append(first)
        news.append(second)
        news.append(third)
        return render(request, 'index.html', {'news':news, 'videos':videos})
    except:
        return render(request, 'index.html')
