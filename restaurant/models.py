from django.db import models

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    inventory = models.SmallIntegerField()
    
    def __str__(self):
        return f'{self.title} : {str(self.price)}'

class Booking(models.Model):
    name = models.CharField(max_length=200)
    no_of_guests = models.SmallIntegerField()
    booking_date = models.DateField()

    def __str__(self): 
        return self.name