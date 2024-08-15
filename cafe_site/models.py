from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=False, blank=False)
    subject = models.CharField(max_length=255, blank=False)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-created_date']

