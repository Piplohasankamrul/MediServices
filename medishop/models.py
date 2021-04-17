from django.db import models

# Create your models here
class Slidding(models.Model):
    discount = models.CharField(max_length=100)
    productName = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2,max_digits=15,default=0)
    image = models.ImageField(blank=True,upload_to='slidder/')

    def __str__(self):
        return self.productName

    def ImageUrl(self):
        if self.image:
            return self.image.url
        else:
            return ""


class Cover(models.Model):
    image = models.ImageField(blank=True,upload_to='Cover/')


    def ImageUrl(self):
        if self.image:
            return self.image.url
        else:
            return ""