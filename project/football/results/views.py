from django.shortcuts import render
from .models import Results
# Create your views here.
def results(request):
    results = Results.objects.all()

    return render(request, 'results.html', {'results':results})