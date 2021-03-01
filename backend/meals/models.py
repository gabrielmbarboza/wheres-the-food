from django.db import models


class Meal(models.Model):
    class Meta:
        db_table = 'meals'
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name
