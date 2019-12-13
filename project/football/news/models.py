from django.db import models
from PIL import Image

size_300 = (300,300)
class News(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='pics')
    date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]+'...'
    #
    # def sImage(self):
    #     return self.image.thumbnail(size_300)


# Create your models here.
