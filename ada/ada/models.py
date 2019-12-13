from django.db import models

class Buyer(models.Model):
    name=models.CharField(max_length=50)
    surname=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    password2=models.CharField(max_length=50)
    def __str__(self):
        return "Buyer %s %s"  % (self.name , self.surname)




