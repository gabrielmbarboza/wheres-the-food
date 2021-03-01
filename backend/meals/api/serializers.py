from meals.models import Meal
from rest_framework.serializers import ModelSerializer


class MealSerializer(ModelSerializer):
    class Meta:
        model = Meal
        fields = ['name', 'description', 'price']
