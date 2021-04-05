from kitchens.models import Kitchen
from rest_framework.serializers import ModelSerializer
from addresses.api.serializers import AddressSerializer
from meals.api.serializers import MealSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer


class KitchenSerializer(WritableNestedModelSerializer, ModelSerializer):
    address = AddressSerializer(required=True)
    meals = MealSerializer(many=True)

    class Meta:
        model = Kitchen
        fields = ['id', 'name', 'opening_hours', 'meals', 'address']

    

