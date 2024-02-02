from django.db import models
from categories.models import Categories
from datetime import datetime
# Create your models here.

class Items(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    type_choice = {
        (0, 'Veg'),
        (1, 'Non-Veg')
    }
    type = models.IntegerField(default=0, choices=type_choice)
    price = models.FloatField()
    created = models.DateTimeField(default=datetime.now)
    active = models.BooleanField(default=1)


    def __str__(self):
        return self.name

