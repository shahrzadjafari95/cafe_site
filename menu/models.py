from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Menu(models.Model):
    # image = models.ImageField()
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    content = models.TextField()
