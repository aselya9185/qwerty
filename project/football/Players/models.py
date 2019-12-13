from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=250)
    lastName = models.CharField(max_length=250)
    fc = models.CharField(max_length=250)
    smallImg = models.ImageField(upload_to='players_image')
    fullimg = models.ImageField(upload_to='players_image')
    age = models.IntegerField()
    inform = models.TextField()
    position = models.CharField(max_length=250)



    def __str__(self):
        return self.name +" "+self.lastName





# Create your models here.
