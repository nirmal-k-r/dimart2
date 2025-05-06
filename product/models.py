from django.db import models

# Create your models here.
class Product(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    quantity=models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # image = models.ImageField(upload_to='products')
    imageUrl = models.CharField(max_length=255)

    def __str__(self):
        return self.name