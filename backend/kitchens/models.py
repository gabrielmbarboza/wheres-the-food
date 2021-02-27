from django.db import models


class Kitchen(models.Model):
    class Meta:
        db_table = 'kitchens'
    name = models.CharField(max_length=250)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name
