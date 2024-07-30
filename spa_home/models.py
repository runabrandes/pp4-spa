from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Service(models.Model):
    """
    Offered services

    -`service` is a CharField that holds
     the name of the service provided
    -`description` is a TextField which
    holds a description of the different service offered
    -`price` is a DecimalField that holds
     the price of the corresponding service

    """

    service = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.service
