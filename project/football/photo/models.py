from django.db import models
import urllib

class Photo(models.Model):
    photo = models.ImageField(upload_to='FootballPhotos')


class Video(models.Model):
    title = models.CharField(max_length=250)
    videoUrl = models.URLField(blank=True)


    def __str__(self):
        return self.title

    def summary(self):
        return self.title[:35]+'...'

    def key(self):
        video_url = urllib.parse.urlparse(self.videoUrl)
        video_id = urllib.parse.parse_qs(video_url.query).get('v')
        return video_id[0]

        # len1 = len(self.videoUrl)
        # return self.videoUrl[len1-11:]



# Create your models here.



