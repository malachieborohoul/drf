from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=125)
    content = models.TextField(max_length=255)
    price = models.DecimalField(max_length=125)

    @property
    def sale_price(self):
        return (float(self.price)*.8)

