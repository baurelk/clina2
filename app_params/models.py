from django.db import models

class ClothingCat(models.Model):

    name = models.CharField(max_length = 200)
    description = models.TextField()
    defaultPrice = models.FloatField()
    
 
    
    def __str__(self):
        return self.name