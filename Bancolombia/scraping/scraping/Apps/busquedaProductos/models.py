from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField()
    soldOut = models.IntegerField()
    shipping = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.price
    
    def __str__(self):
        return self.soldOut
    
    def __str__(self):
        return self.shipping