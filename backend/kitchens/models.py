from django.db import models
#from meals.models import Meal


class Kitchen(models.Model):
    class Meta:
        db_table = 'kitchens'
    name = models.CharField(max_length=250)
    opening_hours = models.CharField(max_length=250)
    #meals = models.ManyToManyField(Meal)

    def __str__(self):
        return self.name
