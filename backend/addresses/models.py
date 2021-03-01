from django.db import models
from kitchens.models import Kitchen


class Address(models.Model):
    class Meta:
        db_table = 'addresses'
    address = models.CharField(max_length=250)
    neighborhood = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    fed_unit = models.CharField(max_length=250)
    zipcode = models.CharField(max_length=20)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE)
