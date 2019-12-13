from django.db import models

# Create your models here.

class Results(models.Model):
    date = models.DateTimeField()
    FirstClub = models.CharField(max_length=250)
    SecClub = models.CharField(max_length=250)
    Result1 = models.IntegerField()
    Result2 = models.IntegerField()


    def __str__(self):
        return self.FirstClub+'-'+self.SecClub
