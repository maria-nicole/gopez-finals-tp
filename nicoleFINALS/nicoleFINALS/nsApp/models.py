from django.db import models

# Create your models here.

class Ambassador(models.Model):
    ambIdV = models.CharField(max_length=100)
    ambNameV= models.CharField(max_length=100)
    ambPosV= models.CharField(max_length=100)
    ambPnumberV= models.CharField(max_length=100)
    ambEmailV= models.CharField(max_length=100)
    ambSocialV= models.CharField(max_length=100)
    ambDateOfHireV= models.CharField(max_length=100)
    ambBirthdateV= models.CharField(max_length=100)
    ambAdrV= models.CharField(max_length=100)


class Inventory(models.Model):
    itemIdV = models.CharField(max_length=100)
    itemNameV = models.CharField(max_length=100)
    itemQtyV= models.CharField(max_length=100)
    itemPriceV= models.CharField(max_length=100)
    itemDescV= models.CharField(max_length=100)

