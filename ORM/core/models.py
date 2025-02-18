from django.db import models

# Create your models here.
class MarvelModel(models.Model):
    name = models.CharField(max_length=50)
    heroic_name = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.heroic_name