from django.db import models
from meals.models import Meal
from kitchens.models import Kitchen


class Status(models.TextChoices):
    CLOSED = 'CL', 'Fechado'
    OPENED = 'OP', 'Aberto'
    ON_PROCESSING = 'ON', 'Em processamento'
    CANCELLED = 'CA', 'Cancelado'
    ON_DELIVERY = 'OD', 'Em entrega'
    DELIVERED = 'DE', 'Entregue'


class Order(models.Model):
    class Meta:
        db_table = 'orders'
    status = models.CharField(
        choices=Status.choices,
        default=Status.OPENED,
        max_length=2,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE)

    @property
    def total(self):
        total = decimal.Decimal('0.00')
        order_items = OrderItem.objects.filter(order=self)
        for item in order_items:
            total += item.total
        return total


class OrderItem(models.Model):
    class Meta:
        db_table = 'order_items'
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    @property
    def total(self):
        return self.quantity * self.meal.price
