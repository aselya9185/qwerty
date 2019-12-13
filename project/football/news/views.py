from django.shortcuts import render
from .models import News
from django.contrib import messages
from django.db.models import Q
# Create your views here.
def news(request):

    searching = request.GET.get('search', '')

    if searching:
        news = News.objects.filter(title__icontains=searching)
        return render(request, 'news.html', {'news': news})
    else:
        news = News.objects.all()
        return render(request, 'news.html', {'news':news})


def detail(request, pk):
    news = News.objects.get(pk=pk)
    return render(request, 'details.html', {'news':news})