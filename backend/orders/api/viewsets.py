from orders.models import Order
from rest_framework.viewsets import ModelViewSet
# from rest_framework import permissions
from .serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
