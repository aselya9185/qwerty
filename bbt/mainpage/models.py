from django.db import models
from django import forms
from datetime import datetime
from django.contrib.postgres.fields import ArrayField

class Bus(models.Model):
    TYPE_CHOICES = (
        ("Sedentary", "Sedentary"),
        ("Restly", "Restly")
    )
    id = models.AutoField(auto_created=True, primary_key=True, verbose_name='id')
    from_city=models.CharField(max_length=100)
    to_city=models.CharField(max_length=100)
    bus_manufacturer=models.CharField(max_length=100)
    bus_service=models.CharField(max_length=100)
    bus_type = models.CharField(max_length=100,choices=TYPE_CHOICES,default="Sedentary")  # сидячий или лежачий
    bus_amount_seats = models.IntegerField()
    bus_number = models.CharField(max_length=50)

class DateGoingOut(models.Model):
    id=models.AutoField(auto_created=True, primary_key=True, verbose_name='id')
    date_going_out=models.DateTimeField()
    date_arriving=models.DateTimeField()
    bus=models.ForeignKey(Bus,on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.date_going_out.strftime('%Y-%m-%d'))

class Seats(models.Model):
    id=models.AutoField(auto_created=True, primary_key=True, verbose_name='id')
    date=models.ForeignKey(DateGoingOut,on_delete=models.CASCADE)
    status=models.BooleanField(default=True)
    number=models.IntegerField()

class Client(models.Model):
    name=models.CharField(max_length=100)
    surname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    identity_card_number=models.CharField(max_length=100)
    card_number=models.CharField(max_length=1000)

class Image(models.Model):
    id=models.AutoField(auto_created=True, primary_key=True, verbose_name='id')
    images=models.ImageField()
