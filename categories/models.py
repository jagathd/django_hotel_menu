from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200, blank=True)
    active = models.BooleanField(default=1)

    def __str__(self):
        return self.name
