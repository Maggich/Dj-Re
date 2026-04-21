from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    money = models.IntegerField()

class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()

    def __str__(self):
        return self.title