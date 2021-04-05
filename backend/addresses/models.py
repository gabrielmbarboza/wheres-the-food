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
    lat = models.CharField(max_length=30)
    lon = models.CharField(max_length=30)
    kitchen = models.OneToOneField(
        Kitchen, related_name='address', on_delete=models.CASCADE)
