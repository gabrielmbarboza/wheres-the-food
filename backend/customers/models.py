from django.db import models


class Customer(models.Model):
    class Meta:
        db_table = 'customers'
    full_name = models.CharField(max_length=250)
    username = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
