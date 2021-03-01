from meals.models import Meal
from rest_framework.viewsets import ModelViewSet
# from rest_framework import permissions
from .serializers import MealSerializer


class MealViewSet(ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
