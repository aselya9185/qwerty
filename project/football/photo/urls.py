from django.urls import path
from . views import gallery, videos

urlpatterns = [
    path('photo', gallery, name='gallery'),
    path('video', videos, name='videos')
]