from django.db import models

# Create your models here.

class Wishlist(models.Model):
    id=models.AutoField(primary_key=True)
    userId=models.IntegerField()
    productId=models.IntegerField()

    def __str__(self):
        return self.name
