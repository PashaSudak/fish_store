from distutils.command.upload import upload
from email.policy import default
from django.db import models

class Product (models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    availability = models.BooleanField(default = True)
    img = models.ImageField(default = 'no_image.png', upload_to = 'product_image')

    def __str__(self):
        return f'{self.name}'
