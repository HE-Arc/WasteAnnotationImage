from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=70)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
           return self.nom

# Create your models here.
