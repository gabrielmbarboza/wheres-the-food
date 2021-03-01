from orders.models import Order
from rest_framework.serializers import ModelSerializer


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['status', 'created_at', 'kitchen']
