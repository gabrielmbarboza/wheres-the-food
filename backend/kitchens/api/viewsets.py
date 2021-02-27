from kitchens.models import Kitchen
from rest_framework.viewsets import ModelViewSet
# from rest_framework import permissions
from .serializers import KitchenSerializer


class KitchenViewSet(ModelViewSet):
    queryset = Kitchen.objects.all()
    serializer_class = KitchenSerializer
