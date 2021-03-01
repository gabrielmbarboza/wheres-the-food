from kitchens.models import Kitchen
from rest_framework.serializers import ModelSerializer


class KitchenSerializer(ModelSerializer):
    class Meta:
        model = Kitchen
        fields = ['name', 'opening_hours']
