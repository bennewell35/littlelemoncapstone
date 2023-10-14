# restaurant/models.py

from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    inventory = models.PositiveIntegerField()

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.PositiveIntegerField()
    BookingDATE = models.DateTimeField()

