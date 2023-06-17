from django.db import models

class Car(models.Model):
    vin = models.CharField(max_length=17, unique=True) # Vehicle Identification Number
    make = models.CharField(max_length=50) # Make of the car
    model = models.CharField(max_length=50) # Model of the car
    year = models.IntegerField() # Year of the car
    timestamp = models.DateTimeField(auto_now_add=True) # Timestamp of the car
    speed = models.FloatField() # Speed of the car
    rpm = models.FloatField() # RPM of the car
    fuel_level = models.FloatField() #fuel level of the car
    temperature = models.FloatField() # Temperature of the car

class CarTelematics(models.Model):
    # Fields defined here
    vin = models.CharField(max_length=17, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    speed = models.FloatField()
    rpm = models.FloatField()
    fuel_level = models.FloatField()
    temperature = models.FloatField()

    def __str__(self):
        return self.vin
