from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    #  define status choices for status field in model
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('sold_out', 'Sold Out'),
        ('coming_soon', 'Coming Soon')]
    image = models.ImageField(upload_to='menu/', null=True, blank=True)
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    status = models.CharField(max_length=50, default='coming_soon', choices=STATUS_CHOICES)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        # Call the original save method to save the image first
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        # Set a uniform size for all images
        desired_size = (136, 136)  # Set your desired size here

        # Resize the image while maintaining aspect ratio
        img = img.resize(desired_size)

        img.save(self.image.path)

    class Meta:
        ordering = ['-created_date']
